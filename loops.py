
# ? ------ For LOOP ------

foods = ['milk', 'bread', 'chocolate', 'rise', 'meal', 'potato']

# * Example one
print('----- Loop one -----')
for food in foods:
    if not food == 'bread' and not food == 'chocolate':
        print(food)

# * Example two
print('----- Loop two -----')
for food in foods:
    if food.startswith('r'):
        print('food start with r')
        break
    print(food)
  
# * Example three
print('----- Loop three -----')
for food in foods:
    if food.startswith('m'):
        print('food start with m')
        continue
    print(food) 

# * Example four
print('----- Loop four -----')
for food in foods:
    print(food.upper())

# * Example five
random_list = ['str', True, 'str2', 84, 'str3', [0, 1, 'asd'], 'asd', [44, False, 'caca']]
print('----- Loop five -----')
for item in random_list:
    if not type(item) == list:
        continue
    for i in item:
        print(i)

# * Example six
print('----- Loop six -----')
for letter in 'Hello World':
    print(letter)

#? ------ WHILE LOOP ------

print('----- While loop one -----')
my_list = ['Red', 'Green','Blue', 1, 2, 3,]

i = 0

while i < len(my_list):
    print(my_list[i])
    i = i + 1
