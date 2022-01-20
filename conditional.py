
#* Example one

x = 11

if x > 60:
    print(f"{x} is greater than 60")
elif x < 60:
    print(f"{x} is less than 60")
else:
    print(f"{x} is equal to 60")

#* Example two

name = 'John'
lastname = 'Cena'

if name == 'John':
    if lastname == 'Cena':
        print('You are John Cena')
    else:
        print('You are not John Cena')
else:
    print('You are not John')

#* Example three

y = 11

if y > 0 and y < 10:
    print(f"{y} is greader than 0 asd less than 10")

if y == 20 or y == 10:
    print(f"{y} is equal to 20 or 10")

if (not(x == y)):
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")