
#* Normal Class

class Person:
    def greet(self):
        print('Hello from person class')

    def sayXd():
        print('XD')

john = Person() # Creating an object with person class
john.greet()

#* Constructor class
class BrawlLegend:

    """
        '__init__' is the constructor function 
        and inside her we must to pass the 
        params to define the object propertis
    """
    def __init__(self, name, weapon1, weapon2):
        self.name = name
        self.firts_weapon = weapon1
        self.second_weapon = weapon2


    def introduce_herself(self):
        print(f'My name is {self.name}, and i use {self.firts_weapon} and {self.second_weapon}')

new_legend = BrawlLegend('Orion', 'Lance', 'Rocket lance') # Creating an object with person class and passing the arguments
new_legend.introduce_herself()

#* Class inheritance

# Parent Class
class AnimalBehaviour:
    def move(self):
        print('Moving')

    def breathe(self):
        print('Animal breating')

# Children class
class Cat(AnimalBehaviour):
    def __init__(self, name, breed, lives):
        self.name = name
        self.breed = breed
        self.lives_count = lives

    def dead(self):
        if self.lives_count == 0:
            print('the cat is completely dead')
        else:
            self.lives_count -= 1
            print(f'Cat lives: {self.lives_count}')

my_cat = Cat('Azul', 'Siamez', 10) # creating an object with cat class 
my_cat.breathe()
my_cat.move()
print(my_cat.lives_count)


#? Testing --------------------------
# for num in range(1, 12):
#     my_cat.dead()
#? Testing -------------------------