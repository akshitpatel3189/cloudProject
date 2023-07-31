from flask import Flask, request, render_template, redirect, url_for, session
import requests
import os
import boto3

def generate_secret_key():
    return os.urandom(24).hex()

app = Flask(__name__)
app.secret_key = generate_secret_key()

# Initialize the Secrets Manager client
secrets_manager_client = boto3.client('secretsmanager')

# Retrieve the secret value from Secrets Manager
secret_name = 'apiUrl'
response = secrets_manager_client.get_secret_value(SecretId=secret_name)
secret_data = response['SecretString']
API_GATEWAY_ENDPOINT = secret_data

# Temporary dictionary to store user data
users = {
    'user1': {
        'username': 'user1',
        'email': 'user1@example.com',
        'password': 'password1'
    }
}

# AWS S3 configuration
BUCKET_NAME = 'cloudprojtak'

# Replace with your AWS credentials
aws_access_key_id = 'ASIA2RFGTH4RRCQWJJH2'
aws_secret_access_key = 'HjPnowL4CbHNzgDkE98sBAGhlUoT8PHwvegOehI2'
aws_region = 'us-east-1'
aws_session_token = 'FwoGZXIvYXdzEDAaDH/5M/JwA83ylFl1XiLAAW8YFPcQ27Huf1aJ0V4rJiDicr5J0Tkisss7FDV53Bmpy/4IPBjLWU9swFDA8rF4ARLLoNbaJSKPUOoFEy/JkCxaflo/G4uELM+TMXGSY2lC1uSG5GrMkWj1MNlPCMJ4bkpVlzBkWb8CGAgbtozrV3N7qYiwNrnFXNA4XJBjwp2g3a6etIQ6boYjmux7w2mulRVHhfq/oj2/NOOl9sCL0kRmBGFswqG3NI+GleR7yqP0zjaUwf2QRYlL6aE8hDtsKCjRpZ2mBjItRU96UUAKU5ec0aJ6ShIMAvogr6X0h0+NqXBHw6HDT30easLuCvnthZ1ONeJG'


s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region,
                        aws_session_token=aws_session_token)

def validate_email(email):
    # Basic email validation 
    return '@' in email and '.' in email

def validate_password(password):
    # Basic password validation
    return len(password) >= 4

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username and email and password and validate_email(email) and validate_password(password):
            if username not in users:
                users[username] = {'username': username, 'email': email, 'password': password}

                # Send the email to the AWS API Gateway
                data = {'email': email}
                try:
                    response = requests.post(API_GATEWAY_ENDPOINT, json=data)
                    if response.status_code == 200:
                        return redirect(url_for('login'))
                    else:
                        return "Error: Unable to create SNS topic and subscribe."
                except requests.exceptions.RequestException as e:
                    return f"Error: {e}".format(e)
                
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists and the provided password is correct
        for user_data in users.values():
            if user_data['email'] == email and user_data['password'] == password:
                session['username'] = user_data['username']
                return redirect(url_for('upload'))

        # Invalid email or password
        return render_template('login.html')

    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            message='No file part'
            return render_template('file_upload.html', message=message)
        
        file = request.files['file']
        
        # Check if the file is selected
        if file.filename == '':
            message='No file selected'
            return render_template('file_upload.html', message=message)

        '''
            Adapted from
                https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html '''
        # Check if the bucket exists, create if not
        try:
            s3_client.head_bucket(Bucket=BUCKET_NAME)
        except:
            s3_client.create_bucket(Bucket=BUCKET_NAME)
            print("Bucket created successfully!")

        '''
            Adapted from
                https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html '''
        # Upload the file to S3
        try:
            s3_client.upload_fileobj(file, BUCKET_NAME, file.filename)

            # Store the uploaded filename in the session
            session['uploaded_filename'] = file.filename

            return redirect(url_for('success'))
        except Exception as e:
            message='An error occurred: {}'.format(e)
            return render_template('file_upload.html', message=message)
    return render_template('file_upload.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    message='Text extrated and send to mail'
    return render_template('success.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
