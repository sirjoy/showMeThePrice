"""Read the scanner input"""
import pandas as pd


def infinite_loop_get_price():
    """Main"""
    # Read data base
    data_base = get_db()
    available_codes = get_available_codes(data_base)

    while True:
        barcode = read_barcode()
        print(f"Barcode scanned: {barcode}")
        get_product_price(available_codes, barcode, data_base)


def get_available_codes(data_base):
    available_codes = list(data_base.code.unique())
    return available_codes


def get_db():
    data_base = pd.read_csv("data/productos_donde_pekas.csv", dtype={'code': str})
    return data_base


def get_product_price(available_codes, barcode, data_base):
    price, product_name = None, None
    if barcode in available_codes:
        record = data_base.loc[data_base.code == barcode, ['price', 'product']]
        price, product_name = record['price'].values[0], record['product'].values[0]
        print(f"Producto: {product_name}")
        print(f"Precio: ${price}")
    else:
        print("Producto no esta en base de datos")
    return price, product_name


def read_barcode():
    barcode = input("Scan barcode: ")
    barcode = barcode.lstrip('0')
    return barcode

#
# if __name__ == '__main__':
#     main()
