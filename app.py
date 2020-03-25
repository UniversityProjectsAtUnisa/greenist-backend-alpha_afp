from flask import Flask
import config


app = Flask(__name__)

app.config.from_object('config.DevConfig')
app.config.from_envvar('~/.env', silent=True)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
