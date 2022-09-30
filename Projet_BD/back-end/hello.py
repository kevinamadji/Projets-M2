from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == "__main__":
    app.run()
