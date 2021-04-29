from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime


class Customer(db.Model, UserMixin):
    loginName = db.Column(db.String(150), primary_key=True)
    password = db.Column(db.String(150))
    fullName = db.Column(db.String(150))
    phoneNumber = db.Column(db.Integer)
    address = db.Column(db.String(150))
    trusted = db.Column(db.Integer, default=0, nullable=False)
    not_trusted = db.Column(db.Integer, default=0, nullable=False)
    orderings = db.relationship('Ordering')
    comment = db.relationship('Comments')
    waitlists = db.relationship('Waitlist')

    def get_id(self):
        return (self.loginName)

    # def is_authenticated(self):
    # 	return True


class Manager(db.Model, UserMixin):
    loginName = db.Column(db.String(150), primary_key=True)
    password = db.Column(db.String(150))
    fullName = db.Column(db.String(150))
    phoneNumber = db.Column(db.Integer)
    address = db.Column(db.String(150))
    trusted = db.Column(db.Integer, default=0, nullable=False)
    not_trusted = db.Column(db.Integer, default=0, nullable=False)

    def get_id(self):
        return (self.loginName)


class Books(db.Model):
    ISBN = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(150))
    Publisher = db.Column(db.String(150))
    PublicationDate = db.Column(db.DateTime)
    NumberOfPages = db.Column(db.Integer)
    NumberOfCopies = db.Column(db.Integer)
    Price = db.Column(db.Float)
    Keywords = db.Column(db.String(500))
    SubjectOfBook = db.Column(db.String(150))
    authors = db.relationship('Author')
    orderings = db.relationship('Ordering')
    comment = db.relationship('Comments')
    waitlists = db.relationship('Waitlist')


class Author(db.Model):
    authorID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    ISBN = db.Column(db.Integer, db.ForeignKey('books.ISBN'))


class Stock(db.Model):
    DeliveryDate = db.Column(db.DateTime(timezone=True),
                             primary_key=True, default=func.now())
    NumberOfBooks = db.Column(db.Integer)


class Ordering(db.Model):
    ISBN = db.Column(db.Integer, db.ForeignKey('books.ISBN'), primary_key=True)
    loginName = db.Column(db.String(150), db.ForeignKey(
        'customer.loginName'), primary_key=True)
    NumberOfCopies = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime(timezone=True), default=func.now())


class Comments(db.Model):
    ISBN = db.Column(db.Integer, db.ForeignKey('books.ISBN'), primary_key=True)
    loginName = db.Column(db.String(150), db.ForeignKey(
        'customer.loginName'), primary_key=True)
    Rating = db.Column(db.Integer)
    ShortText = db.Column(db.String(500))
    Useless = db.Column(db.Integer, default=0, nullable=False)
    Useful = db.Column(db.Integer, default=0, nullable=False)
    VeryUseful = db.Column(db.Integer, default=0, nullable=False)


class Waitlist(db.Model):
    ISBN = db.Column(db.Integer, db.ForeignKey('books.ISBN'))
    loginName = db.Column(db.String(150), db.ForeignKey('customer.loginName'))
    NumberOfCopies = db.Column(db.Integer)
    Token = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Rent(db.Model):
    ISBN = db.Column(db.Integer, db.ForeignKey('books.ISBN'), primary_key=True)
    loginName = db.Column(db.String(150), db.ForeignKey(
        'customer.loginName'), primary_key=True)
    NumberOfCopies = db.Column(db.Integer)
    BuyDate = db.Column(db.DateTime(timezone=True), default=func.now())
    EndDate = db.Column(db.DateTime(timezone=True), default=func.now()+1)


# def init_db():
 #   db.create_all()


# if __name__ == '__main__':
 #   init_db()
