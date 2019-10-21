from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')

class NewAccountForm(FlaskForm):
  account_type = SelectField(
                    'Account Type:',
                    choices=[('checking',  'Checking               (Min balance: $50)'), 
                             ('saving',    'Saving                 (Min balance: $500)'),
                             ('monMarket', 'Money Market           (Min balance: $100)'),
                             ('cd',        'Certificate of Deposit (Min Balance: $1,000)'),
                             ('ira',       'IRA CD                 (Min Balance: $5,0000)')]
                )
  deposit        = FloatField('Initial Deposit', validators=[DataRequired()])
  address        = StringField('Current Address', validators=[DataRequired()])
  employer       = StringField('Current Employer', validators=[DataRequired()])
  monthly_income = StringField('Monthly Income', validators=[DataRequired()])
  submit         = SubmitField('Send Application')