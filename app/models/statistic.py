from app import db
from dataclasses import dataclass


@dataclass
class Statistic(db.Model):
    
    __tablename__ = 'statistics'
    id =db.Column('id',db.Integer, primary_key=True)
    events_participated = db.Column('events_participated', db.String(255))
    wins = db.Column('wins', db.String(255))
    losses = db.Column('losses', db.String(255))
    goals_scored = db.Column('goals_scored', db.String(255))
    assists = db.Column('assists', db.String(255))
    heights = db.Column('heights', db.String(255))
    weight = db.Column('weight', db.String(255))