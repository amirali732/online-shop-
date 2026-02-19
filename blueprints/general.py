from flask import Blueprint

app = Blueprint("general",__name__)

@app.route('/')
def hello_world():
    return ('amirali')