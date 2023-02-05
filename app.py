from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/home")
def FUN_root():
    return render_template("index.html")


@app.route("/resources")
def FUN_resource():
    data = {
        "Modules": 15,
        "Subject": "Data Structures and Algorithms",
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
