from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

