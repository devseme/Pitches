from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


    # the post table
class Post(db.Model):  
    _tablename_ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    category= db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('Comment', backref='post', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')

    # save post

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Post {self.title}'

class Upvote(db.Model):
    tablename = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(post_id=id).all()
        return upvote

    def repr(self):
        return f'{self.user_id}:{self.post_id}'


class Downvote(db.Model):
    tablename = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        downvote = Downvote.query.filter_by(post_id=id).all()
        return downvote

    def repr(self):
        return f'{self.user_id}:{self.post_id}'    

    # user table
class User(UserMixin, db.Model):  
    _tablename_ = 'user'
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    

    # save user
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    # generate password hash
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # check password
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # login manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def _repr_(self):
        return f'User {self.username}'


# comment table
class Comment(db.Model):
    _tablename_ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Comment {self.content}'