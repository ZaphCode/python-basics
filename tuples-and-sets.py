# ---- Tuples ----

tuple_demo = ('sunday','monday','tuesday')

print(type(tuple_demo))

# print(dir(tuple_demo))

print(tuple_demo)
print(tuple_demo[1])
print(len(tuple_demo))

# consctructor
tuple_demo2 = tuple(('red', 'green', 'blue'))
print(tuple_demo2)

# ---- Sets ----

set_demo = {1, 2, 3, 'a', 'b', 'c'}

print(type(set_demo))

# print(dir(set_demo))

print('a' in set_demo)

set_demo.add('d')
print(set_demo)

set_demo.remove('1')
print(set_demo)
