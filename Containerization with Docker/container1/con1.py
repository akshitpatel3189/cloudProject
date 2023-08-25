from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    json_data = request.get_json()

    file_name = json_data.get('file')
    product = json_data.get('product')

    file = "/app/data/"+file_name

# Validate input JSON
    if not file_name:
        return jsonify({'file': None, 'error': 'Invalid JSON input.'}), 400
    
    # Verify file existence
    if not check_file_exists(file):
        return jsonify({'file': file_name, 'error': 'File not found.'}), 404

    response = requests.post('http://container2:6001/process_csv', json={'file': file_name, 'product': product})

    return response.json()

def check_file_exists(file):
    # file_path = os.path.join('.', file_name)

    if os.path.isfile(file):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)