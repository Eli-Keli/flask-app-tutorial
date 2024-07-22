# URL Building

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def home():
    about_url = url_for("about")
    user_url = url_for("show_user_profile", username="Eli")
    return f'Welcome to the Home Page! <br> About: {about_url} <br> User: {user_url}'

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {username}"


if __name__ == "__main__":
    app.run(debug=True)