# Simple Dictionary

alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])



print(alien_0['points'])

# Working with dictionaries

new_points = alien_0['points']

print(f"You just earned {new_points} points!")

# Adding new value pair in dictionary

print("\nAdding new value pair in dictionary\n")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Adding element in empty list

print('\nAdding element in empty list\n')

em_li = {}

em_li['color'] = 'red'
em_li['points'] = 15

print(em_li)

# Modifying values in dictionary

print('Modifying values in dictionary')

print('\nPrevious value of dictionary\n')
alien_0 = {'color' : 'green'}
print(alien_0)

print('\nNew value of dictionary\n')
alien_0['color'] = 'yellow'
print(alien_0)


