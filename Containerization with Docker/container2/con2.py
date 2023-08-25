import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_csv', methods=['POST'])
def process_csv():
    json_data = request.get_json()

    file_name = json_data.get('file')
    product = json_data.get('product')

    if not file_name:
        return jsonify({'file': None, 'error': 'Invalid JSON input.'}), 400

    try:
        df = pd.read_csv("/app/data/" + file_name)
    except pd.errors.EmptyDataError:
        return jsonify({'file': file_name, 'error': 'File not found.'}), 404
    except pd.errors.ParserError:
        return jsonify({'file': file_name, 'error': 'Input file not in CSV format.'}), 400

    sum_amount = df[df['product'] == product]['amount'].sum()

    return jsonify({'file': file_name, 'sum': int(sum_amount)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
