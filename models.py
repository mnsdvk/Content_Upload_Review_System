from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.Integer, nullable=True)
    homepage = db.Column(db.String(255), nullable=True)
    original_language = db.Column(db.String(50), nullable=False)
    original_title = db.Column(db.String(255), nullable=False)
    overview = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.Date, nullable=False)
    revenue = db.Column(db.BigInteger, nullable=True)
    runtime = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(50), nullable=True)
    vote_average = db.Column(db.Float, nullable=True)
    vote_count = db.Column(db.Integer, nullable=True)
    production_company_id = db.Column(db.Integer, nullable=True)
    genre_id = db.Column(db.Integer, nullable=True)
    languages = db.Column(db.String(255), nullable=True)

