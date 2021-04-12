from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/post', methods =['POST'])
def submit():
    if request.method == 'POST':
        post = request.form["new post"]
        type = request.form["type"]
        if post == '' or type == '':
            return render_template("index.html", message='Missing Fields')
        return render_template("confirm.html")

if __name__ == "__main__":
    app.run(debug=True)