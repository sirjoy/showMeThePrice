"""Web app"""
from flask import Flask
from read_scanner import read_barcode, get_product_price, get_available_codes, get_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>App ShowMeThePrice is running!</p>"


@app.route("/barcode")
def show_barcode():
    barcode = read_barcode()
    data = get_db()
    price, name = get_product_price(get_available_codes(data), barcode, data)
    return f"<p>Barcode: {barcode}, Precio: {price} - Producto: {name}</p>"
