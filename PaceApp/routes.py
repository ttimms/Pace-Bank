from flask import render_template, redirect, flash, url_for
from PaceApp import PaceApp, db
from PaceApp.forms import LoginForm, NewAccountForm
from flask_login import current_user, login_user, logout_user, login_required
from PaceApp.dbModels import Customer, Account

@PaceApp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    customer = Customer.query.filter_by(username=form.username.data).first()
    if customer is None or not customer.check_password(form.password.data):
      flash('Username or password is incorrect. Please try again.')
      return redirect(url_for('login'))
    login_user(customer, remember=False)
    return redirect(url_for('index'))
  return render_template('login.html', title='Pace - Login', form=form)

@PaceApp.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))

@PaceApp.route('/')
@PaceApp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
  accounts = Account.query.filter_by(customer_id=current_user.id)
  form = NewAccountForm()
  if form.validate_on_submit():
      account = Account()
      db.session.add(account)
      db.session.commit()

      if form.account_type.data == 'checking':
        account.account_number = str(account.id + 10000000000)
        account.interest_rate = 0

      elif form.account_type.data == 'saving':
        account.account_number = str(account.id + 20000000000)
        account.interest_rate = 2

      elif form.account_type.data == 'monMarket':
        account.account_number = str(account.id + 30000000000)
        account.interest_rate = 5

      elif form.account_type.data == 'cd':
        account.account_number = str(account.id + 40000000000)
        account.interest_rate = 8
        account.maturity_date = date.today() + relativedelta(months=+6)

      elif form.account_type.data == 'ira':
        account.account_number = str(account.id + 50000000000)
        account.interest_rate = 10
        account.maturity_date = date.today() + relativedelta(months=+60)

      else:
        return

      account.amount = form.deposit.data
      account.customer_id = current_user.id
      db.session.add(account)
      db.session.commit()

  return render_template('index.html', title='Pace - Home', accounts=accounts, form=form)