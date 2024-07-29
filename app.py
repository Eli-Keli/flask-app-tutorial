
#* Sessions
from flask import Flask, flash, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "mysecretkeyisflask" # Configure secrect key

@app.route("/")
def index():
    return render_template("index.html")

#Flashing a message
@app.route("/flash-message")
def flash_message():
    flash("This is a flashed message")
    return redirect(url_for("index"))

# Flashing messages with category
@app.route("/flash-category")
def flash_category():
    flash("This is an info message", "info")
    flash("This is a warning message", "warning")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)