
#* Logging
import logging
from flask import Flask

app = Flask(__name__)
app.secret_key = "mysecretkeyisflask" # Configure secrect key

# Customizing Logging Configuration

# Set up logging to a file 
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

# Basic Logging
@app.route("/")
def index():
    app.logger.info("Processing default request")
    return "Hello, Flask!"

@app.route("/error")
def error():
    app.logger.error("Error occured")
    return "An error occured!", 500

# Using Different Log Levels
@app.route("/debug")
def debug():
    app.logger.debug("This is a debug message")
    return "Debug message logged"

@app.route("/info")
def info():
    app.logger.info("This is a info message")
    return "Info message logged"

@app.route("/warning")
def warning():
    app.logger.warning("This is a warning message")
    return "Warning message logged"

@app.route("/critical")
def critical():
    app.logger.critical("This is a critical message")
    return "Critical message logged"

if __name__ == "__main__":
    app.run(debug=True)