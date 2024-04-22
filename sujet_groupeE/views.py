from flask import Flask, render_template
app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')
@app.route("/")
def index():
    return render_template("index.html")
