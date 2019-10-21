from PaceApp import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class Customer(UserMixin, db.Model):
  id              = db.Column(db.Integer, primary_key=True)
  username        = db.Column(db.String(64), index=True, unique=True)
  password_hash   = db.Column(db.String(128))
  email           = db.Column(db.String(120), index=True, unique=True)
  address         = db.Column(db.String(128))
  employer        = db.Column(db.String(64))
  monthly_income  = db.Column(db.Integer)
  accounts        = db.relationship('Account', backref='owner', lazy='dynamic')

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return '<Customer: {}>'.format(self.username)

  @login.user_loader
  def load_user(id):
    return Customer.query.get(int(id))


class Account(db.Model):
  id              = db.Column(db.Integer, primary_key=True)
  account_number  = db.Column(db.String(11))
  amount          = db.Column(db.Float)
  min_deposit_bal = db.Column(db.Float)
  interest_rate   = db.Column(db.Float)
  maturity_date   = timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  customer_id     = db.Column(db.Integer, db.ForeignKey('customer.id'))

  def __repr__(self):
    return '<Acount Number: {}>'.format(self.account_number)
