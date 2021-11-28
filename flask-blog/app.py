
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test_user:test_pw@flask-blog-db/test_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test_user:test_pw@172.18.0.2:3306/test_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def test():
    return "test endpoint is healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


