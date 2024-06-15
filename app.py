from flask import Flask

app = Flask(__name__)


@app.route("/")
def inex():
    return "Response Data"


@app.route("/another")
def another():
    return "Another Response"


if __name__ == "__main__":
    app.run(debug=True)
