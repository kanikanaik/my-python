from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/api/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
