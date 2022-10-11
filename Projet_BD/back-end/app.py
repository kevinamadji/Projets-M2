from flask import Flask, make_response, redirect, url_for, render_template, request
from models import Personnage, Item, db
from sqlalchemy.sql import func




def creer_application():
    app_flask = Flask(__name__)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == "__main__":
    app.run()
