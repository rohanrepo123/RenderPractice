from flask import Flask , render_template

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]

@app.route('/')
def make():
    return '<h1>This is a good thing</h1>'

@app.route('/base')
def make_a():
    return render_template('base.html')

@app.route('/base/retro')
def makeer():
   return render_template('mohan.html')