from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def index() -> str:
    return "Hola"


@app.route("/mundo")
def index() -> str:
    return "mundo"