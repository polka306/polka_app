from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.config.from_object(config)

#ORM
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register/')
def register():
    return render_template('register.html')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('item_set'))
    item_type = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(200), nullable=False)
    item_reinforce_level = db.Column(db.Integer, nullable=False)
    item_reinforce_chance = db.Column(db.Float, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

