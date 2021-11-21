
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def test():
    return "test endpoint is healthy"

app.run(host='0.0.0.0', port=8080)

