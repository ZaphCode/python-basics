demo_list = ['str', 69, True, [0.25, 'asd', None]]

# Constructor list
constr_list = list((1, 'str', False))
rang = list(range(1, 10))

print(rang)
print(constr_list)

# ---- Properties and Methods ----

print(len(demo_list)) # Shows the number of items
print(demo_list[3][1]) # Shows the element by the index defined
print(demo_list[-1]) # Shows the element by the inversed index defined
print('str' in demo_list) # Its like and include method in js, this return a boolean value

# Change values
colors = ['red', 'green', 'blue']
print(colors)
colors[1] = 'yellow'
print(colors)

colors.append('white') # add a new value to the list
print(colors)

colors.extend(['black', 'silver']) # add new values to the list
print(colors)

colors.pop() # remove the last value from the list
print(colors)

colors.pop(2) # remove a value from the list by the index defined
print(colors)

colors.sort() # sort items alphabetically (a-z)
print(colors)

print(colors.sort(reverse=True)) # sort items alphabetically (invert z-a)
print(colors)
