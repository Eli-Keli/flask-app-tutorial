# Routing and Variable rules

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page!"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'


if __name__ == "__main__":
    app.run(debug=True)