# HTTP Methods

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

@app.route('/post/<int:post_id>', methods=["POST", "GET"])
def show_post(post_id):
    if request.method == "POST":
        return f'Creating or updating post {post_id}'
    else:
        return f'Post ID: {post_id}'


if __name__ == "__main__":
    app.run(debug=True)