# A list is a collection of items in a particular order. 
# In Python, square brackerts ([ ]) indicate a list, and individual elements in the list are separated by commas.

bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Accessing elements in a list:
# We can access the element by the index of the element

print(bicycles[0])

print(bicycles[2].upper())

print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].upper()}."
print(message)

# changing, Adding and Removing elemments

print("\nModifying elements in a list\n")

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'

print(motorcycle)

motorcycle[1] = 'ducati'

print(motorcycle)

print('Adding element in the list')

motorcycle.append('yamaha')

print(motorcycle)

# Appending the elements in the empty list

print('--------------------\nAppending the element in the empty list\n')

li_number = []

li_number.append('one')
li_number.append('eleven')

# Inserting the element in the list

print('Inserting the element in the list')

name_li = ['sonu','vidya','shruti']

print(name_li)

name_li.insert(1,'vijay')

print(name_li)

# Removing elements from a list

print('Removing elements from a list using del statement')

del name_li[1]

# pop() in the list

li_car = ['honda', 'audi', 'bmw', 'volkwagan', 'ferari']

print(li_car)

poped_car = li_car.pop()
print(li_car)
print(poped_car)

# Poping elements from any position

last_pop = li_car.pop(0)

print(li_car)

print(last_pop)

# Removing item by the value using the remove()

print('\n------------------------------\nRemoving item by the value using the remove')

print(li_car)

li_car.remove('bmw')

print(li_car)

print()


# Sorting a list permently using sort()

print('\n--------------------------\nShorting a list')

cars = ['ferari', 'toyota', 'bmw', 'audi', 'mercides']

cars.sort()

print(cars)

# Reversing the list

cars.sort(reverse = True)
print('reverse list')
print(cars)

# Sorting a list temporarly with the sorted() fuction

print('\n')

car_new_li = ['bmw', 'audi', 'toyota', 'ferari']

print('Here is the original list')
print(car_new_li)

print('Here is the sorted list')
print(sorted(car_new_li))

print('\nHere is the original list again:')
print(car_new_li)

# List in the revers order

print('\n----------------------\nList in the reverse order')
print('Original List')
print(car_new_li)
print('List in the reverse order')
car_new_li.reverse()
print(car_new_li)

# Finding the length of the list

print('\n-----------------------------\nFinding the length of the list')
print(car_new_li)
print(len(car_new_li))

# Making Numerical Lists

# Using the range() function

print('\nUsing the range() function')

for value in range(1,5):
	print(value)

# Using range() to make a List of Numbers

print('\nUsing range() to make a List of Numbers')

numbers = list(range(1,6))
print(numbers)

# Even numbers in list

print('\nEven numbers')

even_numbers = list(range(2,11,2))
print(even_numbers)

# Squares -- Appending the list

print('\n Squares appending the list')

squares = []

for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)


# Simple Statistics with a list of numbers

print('Simple Statistics with a list of numbers')

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# Slicing the list 

print('\nSlicing the list')

players = ['charles','martina','michael','florence','eli']
print('Originale list = ',(players))
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[:-3])
print(players[-3:])

# Coping the list

print('\nCoping the list')

my_foods = ['pizza', 'falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)


