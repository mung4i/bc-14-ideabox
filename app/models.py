'''Models ORM Classes which are migrated to the database'''
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Users(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    data = db.relationship("Data", backref="users", lazy="dynamic")

    def __init__(self, email, username, first_name, last_name, password = []):
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    '''
    password methods that implement hashing feature extended from werkzeug security module
    '''

    @property
    def password(self):
        raise AttributeError('passwords are protected!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    @login_manager.user_loader
    def load_user(users_id):
        return Users.query.get(int(users_id))


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users_email = db.Column(db.String(60), db.ForeignKey('users.email'))

    def __repr__(self):
        return '<Data: {}>'.format(self.title)


class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<Role: {}>'.format(self.name)
