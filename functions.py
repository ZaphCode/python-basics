
#* Example one: Simple Function

# Definition or creation of the function
def sayHello(): # <- my firs funtion
    print('Hello wolrd')

# Function execution
sayHello()

#* Example two: Function with parameters
def createProd(title, price):
    prod = {
        "title": title,
        "price": price
    }
    print(prod)
createProd('Laptop Rog Strix', 1299.99)

#* Example three: Function with parameter being reused in a loop
list_test = ['Joe', 44, 5, 'Brandon', False, 'Zaph']

def helloToSomeOne(name):
    print(f'Hello {name}!!')

for item in list_test:
    if not type(item) == str:
        continue
    helloToSomeOne(item)

#* Example four: Function with defaut parameter
def saySometing(someWord = "xd"):
    print('The function says:', someWord)

saySometing()
saySometing('Python is nice')

#* Example four: Function that returns something

def add(num1, num2):
    return num1 + num2

print(add(10, 42))
