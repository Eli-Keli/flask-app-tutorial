
#* APIs with JSON
from flask import Flask, request, jsonify


app = Flask(__name__)


# Basic JSON Response
@app.route("/api")
def api_example():
    data = {
        "message": "Hello JSON",
        "status": "success"
    }
    return jsonify(data)

# Returning JSON from a Dictionary
@app.route('/api/direct')
def api_direct():
    return {
        'message': 'Hello, JSON directly!',
        'status': 'success'
    }

# Handling Query Parameters
@app.route('/api/greet')
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f'Hello, {name}!')

# Handling POST Requests
@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Process the data
    processed_data = data.get('key', 'default value')
    return jsonify({'processed_data': processed_data})

# Error Handling in APIs
@app.route('/api/error')
def api_error():
    try:
        raise ValueError('An error occurred!')
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)