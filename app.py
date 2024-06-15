from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def inex():
    return "Response Data"


@app.route("/another")
def another():
    return "Another Response"


@app.route("/test_request")
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route("/exercise_request/<data>")
def exercise_request(data):
    return f"Exercise Request Data: {data}"


if __name__ == "__main__":
    app.run(debug=True)
