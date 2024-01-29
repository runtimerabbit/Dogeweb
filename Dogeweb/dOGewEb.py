import json
from urllib.request import urlopen
import requests
import stripe
from flask import Flask, render_template, url_for, redirect, request, session
import os
from bs4 import BeautifulSoup

app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51KVqOFAt6Q7vrcvsuRD2kWmCrwzKR1SyVOQukHqODeYwcH6HbRTXomMD5FM6UQghIP7Er0kscHfszEpwAuNQHh3s00MuJI6UZj'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51KVqOFAt6Q7vrcvsc3ehuWq9TkjQ2WkEw4lRK7fBwrKlqRCbmNKMyJ8DwaOpVWst42zMRWRt67Ur10yP33SoeY8P00C9CEfDMj'

pic_folder = os.path.join('static', 'imgs')
app.config['UPLOAD_FOLDER'] = pic_folder
url = 'test'
url = str(url)
@app.route('/ProcessUserinfo/ <string:userinfo> ', methods=['POST'])
def ProcessUserinfo(userinfo):
  userinfo = json.loads(userinfo)
  searchInput = userinfo
  print(searchInput)
  torport = 9150
  proxies = {
    'http': "socks5h://localhost:{}".format(torport),
    'https': "socks5h://localhost:{}".format(torport)
  }
  
  return('/')
@app.route('/')
def hello():
  logo = os.path.join(app.config['UPLOAD_FOLDER'], 'Dogeweb.jpg')
  return render_template('index.html', display_logo = logo)

@app.route('/terms')
def terms():
  return render_template('terms.html')

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/donate')
def  donate():
  return render_template('donate.html')
@app.route('/thanks')
def thanks():
  return render_template('sucess.html')
@app.route('/donate5')
def donate5():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'Donation of',
        },
        'unit_amount': 500,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url=url_for('thanks', _external = True),
    cancel_url=url_for('hello', _external = True),
  )
  return redirect(session.url, code=303)
@app.route('/donate10')
def donate10():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'Donation of',
        },
        'unit_amount': 1000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url=url_for('thanks', _external = True),
    cancel_url=url_for('hello', _external = True),
  )
  return redirect(session.url, code=303)

@app.route('/team')
def thankpage():
    p1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Dogeweb.jpg')
    return render_template('team.html', dev1 = p1)
if __name__ == '__main__':
  app.run(debug=True)
