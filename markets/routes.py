from markets import app
from flask import render_template, redirect, url_for
from markets.models import Item, User
from markets.forms import RegisterForm
from markets import db


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

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        use_to_create = User(username=form.username.data,
                             email_address=form.email_address.data, password_hash=form.password1.data)
        db.session.add(use_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html', form=form)
