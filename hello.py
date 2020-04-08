from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"


@app.route("/newpage")
def new_page():
    return "<h1>This is a new page!</h1>"


if __name__ == "__main__":
    app.run()
