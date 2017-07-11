from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/din/<din>")
def view(din):
    return render_template("view.html", din=din)

@app.route("/new")
def create():
    return render_template("new.html")
