from PaceApp import db
from PaceApp.dbModels import Customer, Account
from datetime import date
from dateutil.relativedelta import relativedelta

def ProcessAccountApplication(form):
  account = Account()
  if form.account_type == 'checking':
    account.account_number += 10000000000
    account.interest_rate = 0

  elif form.account_type == 'saving':
    account.account_number += 20000000000
    account.interest_rate = 2

  elif form.account_type == 'monMarket':
    account.account_number += 30000000000
    account.interest_rate = 5

  elif form.account_type == 'cd':
    account.account_number += 40000000000
    account.interest_rate = 8
    account.maturity_date = date.today() + relativedelta(months=+6)

  elif form.account_type == 'ira':
    account.account_number += 50000000000
    account.interest_rate = 10
    account.maturity_date = date.today() + relativedelta(months=+60)

  else:
    return

  account.amount = form.deposit
  db.session.add(account)
  db.session.commit()
