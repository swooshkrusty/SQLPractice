from flask import Flask


app = Flask(__name__)


@app.route("/")
def index1():
    return "Hello, World!!!"


@app.route("/about1")
def about1():
    return "About page"


if __name__ == "__main__":
    app.run(debug=True)
