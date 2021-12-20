from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()
# create models based off of ERD (Database Tables)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    post = db.relationship('Post',backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(150))
    image = db.Column(db.String(300))
    content = db.Column(db.String(300), nullable=False)
    like=db.Column(db.Boolean,nullable=True,default=False)
    dislike=db.Column(db.Boolean,nullable=True,default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, image, content, user_id):
        self.title = title
        self.image = image
        self.content = content
        self.user_id = user_id

class postComments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(300), nullable=False)
    commentposter=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    postId=db.Column(db.Integer,db.ForeignKey('post.id'), nullable=False)
    like=db.Column(db.Boolean,nullable=True,default=False)
    dislike=db.Column(db.Boolean,nullable=True,default=False)
    date_added=db.Column(db.Date,nullable=False,default=date.today)
    

    def __init__(self, comment, commentposter, postId):
        self.comment = comment
        self.commentposter = commentposter
        self.postId = postId




