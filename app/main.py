from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps Bootcamp v1"

@app.route("/health")
def health():
    return "ok"
