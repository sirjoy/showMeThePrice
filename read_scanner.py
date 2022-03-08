"""Read the scanner input"""
import pandas as pd


def main():
    """Main"""
    # Read data base
    data_base = pd.read_csv("data/productos_donde_pekas.csv", dtype={'code': str})
    available_codes = list(data_base.code.unique())

    while True:
        barcode = input("Scan barcode: ")
        barcode = barcode.lstrip('0')
        print(f"Barcode scanned: {barcode}")
        if barcode in available_codes:
            record = data_base.loc[data_base.code == barcode, ['price', 'product']]
            price, product_name = record['price'].values[0], record['product'].values[0]
            print(f"Producto: {product_name}")
            print(f"Precio: ${price}")
        else:
            print("Producto no esta en base de datos")


if __name__ == '__main__':
    main()
