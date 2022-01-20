product = {
#   "key"    "value"
    "title": 'Laptop gamer hp',
    "category": 'laptops',
    "price": 230,
    "quantity": 5
}

person = {
#   "key"   "value"
    "name": 'david',
    "lastname": 'mejia'
}

print(type(product), type(person)) #? -> Type dict

print(product.keys())
# items = product.items()

print('quantity' in product.keys()) #? -> Boolean

# person.clear()
# print(person)

products = [
    {
        "title": 'Mouse gamer',
        "price": 40.25
    },
    {
        "title": 'Laptop Lenovo',
        "price": 999.97
    },
    {
        "title": 'Keyboard corsair',
        "price": 80.00
    }
]