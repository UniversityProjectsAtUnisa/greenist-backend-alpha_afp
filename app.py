from flask import Flask, request
import config
from src.fibonacci import fibonacci


app = Flask(__name__)

app.config.from_object('config.DevConfig')


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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
