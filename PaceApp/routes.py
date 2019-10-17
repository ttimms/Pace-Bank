from flask import render_template, redirect, flash, url_for
from PaceApp import PaceApp
from PaceApp.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from PaceApp.dbModels import Customer

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
    login_user(customer)
    return redirect(url_for('index'))
  return render_template('login.html', title='Login', form=form)

@PaceApp.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))

@PaceApp.route('/')
@PaceApp.route('/index')
@login_required
def index():
  return "Select New Plan feature to be implemented here."