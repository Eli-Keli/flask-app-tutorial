# Unique URLs / Redirection Behavior

from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome to the Home Page!'

@app.route("/about/")
def about():
    return "This is the about page."

@app.route("/contact")
def contact():
    return "This is the contact page."

# Basic Redirection
@app.route('/login')
def login():
    return 'This is the Login Page.'

@app.route('/redirect-to-login')
def redirect_to_login():
    return redirect(url_for('login'))

# Conditional Redirection
@app.route("/profile")
def profile():
    logged_in = request.args.get("logged_in", 'false').lower() == "true"
    if not logged_in:
        return redirect(url_for('login'))
    return 'This is the Profile Page.'

# HTTP Status Codes
@app.route('/permanent-redirect')
def permanent_redirect():
    return redirect(url_for('home'), code=301)

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {username}"


if __name__ == "__main__":
    app.run(debug=True)