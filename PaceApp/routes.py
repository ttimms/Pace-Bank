from flask import render_template
from PaceApp import PaceApp

@PaceApp.route('/')
@PaceApp.route('/login')
def login():
  return render_template('login.html', title='Login')