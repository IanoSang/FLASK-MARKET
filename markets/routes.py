from markets import app
from flask import render_template, redirect, url_for, flash
from markets.models import Item, User
from markets.forms import RegisterForm, LoginForm
from markets import db
from flask_login import login_user


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
                             email_address=form.email_address.data, password=form.password1.data)
        db.session.add(use_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))
    if form.errors != {}:  # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Logged in Successfully! You logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Invalid Username or Password!! Please try again', category='danger')
    return render_template('login.html', form=form)
