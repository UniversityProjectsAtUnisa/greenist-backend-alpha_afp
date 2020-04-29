from flask import request
from .fibonacci import fibonacci

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    return app

app = create_app()


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/fibonacci/<string:n>")
def fib(n):
    if n.isdigit():
        return str(fibonacci(int(n)))
    return "0"
