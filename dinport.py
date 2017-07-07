from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/din/<din>")
def profile(din):
    return render_template("view.html", din=din)