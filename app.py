"""Web app
from tutor: https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
"""
from flask import Flask, render_template, request, url_for, flash, redirect
from read_scanner import read_barcode, get_product_price, get_available_codes, get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


history = []


@app.route('/')
def index():
    return render_template('index.html', messages=history)


@app.route("/barcode")
def show_barcode():
    barcode = read_barcode()
    data = get_db()
    price, name = get_product_price(get_available_codes(data), barcode, data)
    return f"<p>Barcode: {barcode}, Precio: {price} - Producto: {name}</p>"


@app.route('/leer/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        code = request.form['code']

        if not code:
            flash('Un código de barras debe leerse!')
        else:
            history.append({'title': code})
            return redirect(url_for('index'))
    return render_template('create.html')
