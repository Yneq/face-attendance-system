from flask import Flask, render_template, request, jsonify
from attendance import recognize_face

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkin", methods=["POST"])
def checkin():

    img = request.files["image"]

    result = recognize_face(img)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)