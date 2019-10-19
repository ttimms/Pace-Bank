from PaceApp import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import date
from dateutil.relativedelta import relativedelta
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


class Checking_Account(db.Model):
  __abstract__    = True
  __mapper_args__ = {'polymorphic_identity': 'checking_account',
                      'polymorphic_on': 'checking_account_type'}
  account_number  = db.Column(db.String(11))
  amount          = db.Column(db.Float)
  min_deposit_bal = db.Column(db.Float)

  @declared_attr
  def customer_id(cls):
    return db.Column(db.Integer, db.ForeignKey('customer.id'))

  def __repr__(self):
    return '<Acount Number: {}>'.format(self.account_number)

class Saving_Account(Checking_Account):
  id              = db.Column(db.Integer, primary_key=True)
  interest_rate   = db.Column(db.Float)
  __mapper_args__ = {'polymorphic_identity': 'saving_account'}

class Money_Mar_Account(Checking_Account):
  id              = db.Column(db.Integer, primary_key=True)
  interest_rate   = db.Column(db.Float)
  __mapper_args__ = {'polymorphic_identity': 'money_mar_account'}

class CD_Account(Checking_Account):
  id              = db.Column(db.Integer, primary_key=True)
  interest_rate   = db.Column(db.Float)
  maturity_date   = timestamp = db.Column(db.DateTime, index=True, default=date.today() + relativedelta(months=+6))
  __mapper_args__ = {'polymorphic_identity': 'cd_account'}

class IRA_CD(Checking_Account):
  id              = db.Column(db.Integer, primary_key=True)
  interest_rate   = db.Column(db.Float)
  maturity_date   = timestamp = db.Column(db.DateTime, index=True, default=date.today() + relativedelta(months=+6))
  __mapper_args__ = {'polymorphic_identity': 'ira_cd'}