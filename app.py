from flask import Flask, jsonify

from datetime import datetime

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/")
def index():
    current_date = datetime.now().isoformat()
    info = {
        "email": "caseynzewi@gmail.com",
        "current_datetime": current_date,
        "github_url": "<https://github.com/casey216/HNG12_Stage_0>"
    }
    return jsonify(info), 200

if __name__ == "__main__":
    app.run(debug=True)