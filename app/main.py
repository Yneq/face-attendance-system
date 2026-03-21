from flask import Flask, render_template, request, jsonify
from attendance import recognize_face
from db import get_all_logs

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkin", methods=["POST"])
def checkin():
    img = request.files["image"]
    result = recognize_face(img)
    return jsonify(result)

@app.route("/logs")
def logs():
    records = get_all_logs()
    return render_template("logs.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)