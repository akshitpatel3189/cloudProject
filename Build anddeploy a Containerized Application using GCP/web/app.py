from flask import Flask, render_template, request, redirect, jsonify, url_for
import requests

app = Flask(__name__)

name = ''

@app.route('/')
def index():
    '''Based on
       https://flask.palletsprojects.com/en/1.1.x/quickstart/'''
    return render_template('index.html')

# Route for registration
@app.route('/register', methods=['POST'])
def register():
    data = request.form.to_dict()
    register_url = 'https://container1-ilhfrofyqq-uc.a.run.app/register'
    response = requests.post(register_url, json=data)

    if response.ok:
        return render_template('index.html', message='Registration successful')
    else:
        return render_template('index.html', message='Error registering the user')


# Route for login
@app.route('/login', methods=['POST'])
def login():
    global name
    email = request.form.get('loginEmail')
    password = request.form.get('loginPassword')
    data = {
        'email': email,
        'password': password
    }
    login_url = 'https://container2-ilhfrofyqq-uc.a.run.app/login'

    response = requests.post(login_url, json=data)

    if response.ok:
        data = response.json()
        if 'message' in data and data['message'] == 'Login successful':
            name = data.get('name', '')
            return redirect(url_for('dashboard'))
        else:
            return jsonify({'message': 'Error logging in'})
    else:
        return jsonify({'message': 'Error logging in'})


# Route for dashboard
@app.route('/dashboard')
def dashboard():
    global name

    online_users_url = 'https://container3-ilhfrofyqq-uc.a.run.app/online-users'
    response = requests.get(online_users_url)
    
    if response.ok:
        try:
            data = response.json()
            online_users = [user for user in data if user['name'] != name]
            return render_template('dashboard.html', online_users=online_users, name=name)
        except ValueError:
            return jsonify({'message': 'Error retrieving online users: Invalid response format'})
    else:
        return jsonify({'message': 'Error retrieving online users'})


# Route for logout
@app.route('/logout', methods=['POST'])
def logout():
    global name
    logout_url = 'https://container3-ilhfrofyqq-uc.a.run.app/logout'

    # Create the JSON body with the user's name
    data = {
        "name": name
    }
    headers={'Content-type': 'application/json'}
    response = requests.post(logout_url, json=data, headers=headers)
    
    print('Logout User Name:', name)
    return f"Logout successful. <a href='/'>Return to the Main page</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
