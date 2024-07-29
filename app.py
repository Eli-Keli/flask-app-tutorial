
#* Sessions
from flask import Flask, session

app = Flask(__name__)
app.secret_key = "mysecretkeyisflask" # Configure secrect key

@app.route("/")
def index():
    return "<h1>Welcome to the sessions example</h1>"

# Setting session data
@app.route("/set-session")
def set_session():
    session["username"] = "Eli Keli"
    return "<h1>Session data has been set!</h1>"

# Accessing session data
@app.route("/get-session")
def get_session():
    username = session.get("username", "Guest")
    return f"<h2>Welcome, {username}!</h2>"

# Deleting session data
@app.route("/delete-session")
def delete_session():
    session.pop("username", None)
    return "<h1>Session data has been deleted!</h1>"

if __name__ == "__main__":
    app.run(debug=True)