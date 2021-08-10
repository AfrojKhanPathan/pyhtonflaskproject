from app import db
from datetime import datetime

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=True)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return 'Publisher is {}'.format(self.name)

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(500),nullable=True,index=True)
    author = db.Column(db.String(300))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100),unique=True)
    num_page = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    pub_id = db.Column(db.Integer,db.ForeignKey('publication.id'))

    def __init__(self,title,author,avg_rating,format,image,num_page,pub_date,pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_page = num_page
        self.pub_date = pub_date
        self.pub_id = pub_id

    def __repr__(self):
        return 'Book is {}, {}, {}, {}, {}, {}, {}, {}'.format(self.title,self.author,self.avg_rating,self.format,self.image,self.num_page,self.pub_date,self.pub_id)

