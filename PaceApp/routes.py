from flask import render_template
from PaceApp import PaceApp
from PaceApp.forms import LoginForm

@PaceApp.route('/')
@PaceApp.route('/login')
def login():
  loginForm = LoginForm()
  return render_template('login.html', title='Login', form=loginForm)
