from flask import Flask, request, render_template, jsonify

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


@app.route("/show_html")
def show_html():
    return render_template("test_html.html")


@app.route("/exercise_html")
def excersize_html():
    return render_template("exercise.html")


@app.route("/exercise")
def exercise_html():
    my_name = request.args.get("my_name", "")
    return render_template("answer.html", name=my_name)


@app.route("/try_rest", methods=["POST"])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json["name"]
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)


if __name__ == "__main__":
    app.run(debug=True)
