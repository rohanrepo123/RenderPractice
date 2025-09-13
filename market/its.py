from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
# print("Roham")
@app.route('/about')
def about():
    return '<h1>About Page</h1>'