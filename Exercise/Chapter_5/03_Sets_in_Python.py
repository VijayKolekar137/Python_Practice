# Imp --> It is an empty dictionary

a = {}
print(type(a))

# It will create an empty set
b = set()
print(type(b))

# Adding value in the set
b.add(6)
b.add(78)
b.add(6)
b.add(6)
b.add((7,6,9,8))

print(b)

# b.add([7,96,45])            # We can not add the list inside the set
# b.add({78,96,25,12})        # We can not add the dictinoary inside the set

print(len(b))                 # Length of the set

b.remove(6)                   # Removes the value from the set
print(b)

# b.remove(45)                  # It will gives the error because the 45 is not in the set
# print(b)

print(b.pop())
print(b)

