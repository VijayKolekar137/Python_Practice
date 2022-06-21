# Removing all instances of specific values form a list

#Original list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

# After removing specific value from the list
print(pets)