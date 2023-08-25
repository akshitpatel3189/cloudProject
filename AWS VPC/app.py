import boto3
from flask import Flask, request, jsonify
import pymysql
import pymysql.cursors

app = Flask(__name__)

# AWS authentication
aws_access_key_id ='Enter access key here',
aws_secret_access_key ='Enter secret access key here',
aws_session_token_id ='enter session token', #this is optional. I used AWS acadamy so I have to add this filed. If you are using persional account then delete this field
region_name = 'us-east-1'

# Database configuration
db_host = "database-1-instance-1.chfcc7xkg4l3.us-east-1.rds.amazonaws.com"
db_name = "mydb"
db_user = "admin"
db_password = "password"

# Authenticate with AWS
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
    aws_session_token=aws_session_token_id
)

# Check if the 'products' table exists in the database, if not, create it
def create_products_table():
    try:
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()

        cursor.execute("SHOW TABLES LIKE 'products'")
        table_exists = cursor.fetchone()

        if not table_exists:
            cursor.execute("""
                CREATE TABLE products (
                    name VARCHAR(255),
                    price VARCHAR(255),
                    availability BOOLEAN
                )
            """)

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error creating 'products' table:", str(e))


# Store products in the database
@app.route('/store-products', methods=['POST'])
def store_products():
    try:
        data = request.get_json()
        products = data.get('products', [])

        create_products_table()  # Check if the table exists, if not, create it

        # Connect to the RDS database
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()

        # Insert products into the database
        for product in products:
            name = product.get('name')
            price = product.get('price')
            availability = product.get('availability')

            cursor.execute(
                "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)",
                (name, price, availability)
            )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Success.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# List products from the database
@app.route('/list-products', methods=['GET'])
def list_products():
    try:
        create_products_table()  # Check if the table exists, if not, create it

        # Connect to the RDS database
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()

        # Fetch products from the database
        cursor.execute("SELECT name, price, availability FROM products")
        rows = cursor.fetchall()

        # Build the products list
        products = []
        for row in rows:
            product = {
                'name': row['name'],
                'price': row['price'],
                'availability': row['availability']
            }
            products.append(product)

        cursor.close()
        conn.close()

        return jsonify({'products': products}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)