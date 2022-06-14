# Defining a Tuple : Python referes to values that cannot changes as immutable, and an immutable list is called a tuple.

dimension = (200,50)

print(dimension[0])
print(dimension[1])

# If we tried to change the element from the tuple.

#dimension[0] = 220

#print(dimension)

# Tuple with one element

my_t = (3)

# Loopint Through all values in a tuple

print('\nLooping through the tuple')

for dia in dimension:
	print(dia)

# Writing over a tuple

print('\nWriting over a tuple')

print('Original Dimension: ')
for dia in dimension:
	print(dia)

print('\nModified Diamension')

dimension = (400,100)

for dia in dimension:
	print(dia)