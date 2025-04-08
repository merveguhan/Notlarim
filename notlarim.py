#notlarim

#pydantic 1.video

import pydantic

class product:
    def __init__(self, name:str, price:float, in_stock:bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == '__main__':
    #ornek_product = product (name='ornek', price=100, in_stock=True )
    #print(ornek_product.in_stock)

    external_data: = {
        "name": "Laptop",
        "price": "999,99",
        "in_stock": "True"

    }

    product = Product(
        name = external_data.get("name"),
        price = external_data.get("price"),
        in_stock = external_data.get("in_stock")

    )

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))

#2. video pydantic örneği

from pydantic import BaseModel


class ProductPydantic(BaseModel):
    name: str
    price: float
    in_stock: bool


if __name__ == '__main__':

    external_data: = {
        "name": "Laptop",
        "price": "999,99",
        "in_stock": "True"

    }

    product = Product(
        name = external_data.get("name"),
        price = external_data.get("price"),
        in_stock = external_data.get("in_stock")

    )

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))

