# Static Files

from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/css/style.css">
        </head>
        <body>
            <h1>Welcome to the Home Page!</h1>
            <button>Click</button>
            <img src="/static/images/logo.png" alt="Logo">
            <script src="/static/js/script.js"></script>
        </body>
    </html>
    '''

# Using Static Files in Templates
@app.route("/index")
def index():
    return render_template("index.html")

# Custom Static File Route
@app.route('/custom_static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static/css', filename)

if __name__ == "__main__":
    app.run(debug=True)