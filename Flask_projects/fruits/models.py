from os import link
from turtle import title
from fruits import db
from datetime import datetime


class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# fruits model
class Fruit(db.Model, ExtraMixin):
    __tablename__ = 'fruits'
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

#Hacker News model
class HackerNews(db.Model, ExtraMixin):
    __tablename__ = 'hacker_news'
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'created_at': str(self.created_at),
        }

    @classmethod
    def get_all_news(cls):
        return cls.query.all()

# CBS News model
class CbsNews(db.Model, ExtraMixin):
    __tablename__ = 'cbs_news'
    image = db.Column(db.LargeBinary, nullable = False)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)

    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'created_at': str(self.created_at),
        }
    @classmethod
    def get_all_news(cls):
        return cls.query.all()

