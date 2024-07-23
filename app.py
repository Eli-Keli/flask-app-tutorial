
#* File Uploads
from flask import Flask, redirect, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to the Home page.</h1>"

@app.route('/cause-404')
def cause_404():
    # This will cause a 404 error because the route does not exist
    return redirect('/non_existent_page')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500


if __name__ == "__main__":
    app.run(debug=True)