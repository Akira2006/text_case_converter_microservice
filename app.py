from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to convert text case
@app.route("/convert", methods=["POST"])
def convert_text():

    data = request.get_json()

    text = data.get("text")
    case_type = data.get("case")

    if case_type == "upper":
        result = text.upper()

    elif case_type == "lower":
        result = text.lower()

    elif case_type == "title":
        result = text.title()

    else:
        return jsonify({"error": "Unsupported case type"}), 400

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port=5002)