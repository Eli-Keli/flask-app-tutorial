
#* About Responses
from flask import Flask, make_response, jsonify, send_file


app = Flask(__name__)

# Basic Response
@app.route("/")
def index():
    return "Welcome to the Home page."

# Custom Responses
@app.route("/custom")
def custom():
    response = make_response('This is a custom response.')
    response.headers['Content-Type'] = 'text/plain'
    response.status_code = 200
    return response

# JSON Response
@app.route("/json")
def json_example():
    return jsonify(message="This is a JSON response")

# Setting Headers
@app.route("/custom-header")
def custom_headers():
    response = make_response('Hello, with custom headers!')
    response.headers['X-Custom-Header'] = 'CustomHeaderValue'
    return response

# Setting status codes
@app.route('/not-found')
def not_found():
    response = make_response('This resource was not found', 404)
    return response

# File Download
@app.route('/download')
def download_file():
    path = './downloads/download.txt'
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)