products = {
    "jabłko":{
        "quantity": 25,
        "price": 3.7
    },
    "chleb":{
        "quantity": 40,
        "price": 4.10
    },
    "woda": {
        "quantity": 100,
        "price": 2.0
    }
}

def update_product_quantity(product_name, order_quantity):
    products[product_name]["quantity"] -= order_quantity

