#notlarim

#pydantic

#import pydantic

class product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == '__main__':
    ornek_product = product (name='ornek', price=100, in_stock=True )
    print(ornek_product.in_stock)