from flask import request
from .fibonacci import fibonacci

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    return app

app = create_app()


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


@app.route("/fibonacci", methods=["GET"])
def fib():
    n = request.args.get("n")
    print(n)
    if n.isdigit():
        return str(fibonacci(int(n)))
    return "0"
