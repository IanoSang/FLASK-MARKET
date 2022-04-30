from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '56351277281974', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '56351277281974', 'price': 500},
        {'id': 3, 'name': 'Keyboard', 'barcode': '56351277281974', 'price': 500}
    ]
    return render_template('market.html', items=items)

# @app.route('/about/<username>')
# def about_page(username):
#     return f"<h2>About {username}</h2>"
