from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="webapp")

@app.route("/webapp/<path:path>")
def serve_webapp(path):
    return send_from_directory("webapp", path)

@app.route("/")
def index():
    return "Hello! Web App is working."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
