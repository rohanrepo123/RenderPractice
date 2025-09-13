from flask import Flask , render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# db = SQLAlchemy(app)

# class Item(db.model):
#     id = db.Columns(db.integer(), primaray_key=True)
#     name = db.Columns(db.String(length=30), nullable=False , unique=True)
#     price=db.Columns(db.Integer(),nullable=False)
#     barcode = db.Columns(db.String(length=12),nullable=False,unique=True)
#     description = db.Columns(db.String(length=1024,nullable=False,unique=True))

@app.route('/')
def hello_world():
    return '<h1>Hello!I am a Rohan</h1>'
# # print("Roham")f
@app.route('/about')
def about():
    return '<h1>About Page and Alok</h1>'
# @app.route('/<username>')
# def user(username):
#     return f'<h1>Hii This is {username}</h1>'
# @app.route('/')
items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    return render_template('market.html', items=items)