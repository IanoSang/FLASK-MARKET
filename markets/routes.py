from markets import app
from flask import render_template
from markets.models import Item
from markets.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


# @app.route('/about/<username>')
# def about_page(username):
#     return f"<h2>About {username}</h2>"

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
