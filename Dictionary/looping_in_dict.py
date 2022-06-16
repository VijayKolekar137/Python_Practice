# Looping through the dictionary

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
    }
    

for k,v in user_0.items():
    print(f"\n Key : {k}")
    print(f"\n Value: {v}")
    


# Looping through all the keys in a dictionary

print('\nLooping through all the keys in a dictionary')
for key in user_0.keys():
    print(key.title())
    
    
# Looping through all the values in a dictionary

print('\nLooping through all the values in a dictionary')
for val in user_0.values():
    print(val.title())