
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test_user:test_pw@flask-blog-db/test_db'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def test():
    return "test endpoint is healthy"

app.run(host='0.0.0.0', port=8080)
