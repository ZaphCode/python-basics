import time

#* ---- Decorators:  FnA(FnB) => FnC ----

#* Simple decorator example:
print('--------- example one ---------') # -----------

def decorator_basic(fn): # <- The 'fn' param is the function to decore (FnB)
    """
        The wrapper function is the funtion b that 
        decores (add more functionalities) the 'fn' param
        wich is another function. 
    """
    def wrapper(): # <- wrapper function (FnC)
        print('wrapper start')
        result = fn()
        print('wrapper end')
        return result


    return wrapper # <-- The decorator statement will be return the decorator function
@decorator_basic #  <- This is the declarator name or statement
def add():
    return int(6 + 8)


print(add())

#* Decorator with positional arguments example:
print('--------- example two ---------') # -----------

def decorator_with_arguments(fn): # <- Decorator with arguments
    def wrapper_accepting_arguments(arg1, arg2):
        print(f'from the decorator: the arguments are "{arg1}", "{arg2}"')
        fn(arg1, arg2)
    return wrapper_accepting_arguments



@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

#* Decorator with arbitrary arguments example:
print('--------- example three ---------') # -----------

def decorator_with_arbitrary_arguments(fn): # <- Decorator with arbitrary arguments
    def wrapper(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        fn(*args, **kwargs)
    return wrapper

@decorator_with_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

print('--------- example three v2 ---------')

@decorator_with_arbitrary_arguments
def add_funtion_with_arbitrary_arguments(*args, **kwargs):
    if args:
        result = 0
        for item in args:
            try:
                result += item
            except TypeError:
                print('Invalid value: ', item)
                continue
        print(f'total: {result}')
    else:
        print('No args recived')
    if kwargs:
        for key, value in kwargs.items():
            print(f"{key} is {value}")
    else:
        print('No kwargs recived')
    



add_funtion_with_arbitrary_arguments(33, 1, 4, 2, 14, name = 'zaph', password = 'pito123')






#* function with type hints
# def greeting(name: str) -> str:
#     return f'Hello {name}'

# print(greeting(344))

#* Map function
# def map(fn, list):
#     return [fn(item) for item in list]
        
# def squeare(num):
#     return num * num

# mapedList = map(squeare, [1, 2 ,3, 4, 5, 6])
# print(mapedList)