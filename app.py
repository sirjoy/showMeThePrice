"""Web app
from tutor: https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
"""
from flask import Flask, render_template, request, url_for, flash, redirect
from read_scanner import read_barcode, get_product_price, get_available_codes, get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


history = []
data = get_db()


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
            price, name = get_product_price(get_available_codes(data), code, data)
            history.append({'title': code, 'price': price, 'name': name})
            return redirect(url_for('create'))

    if len(history) > 0:
        last_msg = history[-1]
    else:
        last_msg = []
    return render_template('create.html', last_msg=last_msg)
