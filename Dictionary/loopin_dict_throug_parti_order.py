# Looping through a dictonary's keys in a particular order


fav_lang = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

# Without sorted

print('\nWithoud Sorted')

for name in fav_lang.keys():
    print(name)
    
# With sorted 

print('\nWith sorted')
    
for name in sorted(fav_lang.keys()):
    print(name)
    
    
# Putting the dictonary values in set

print('\nPutting dictonary values in the set')

# It will save only unique values in the set 

for lang in set(fav_lang.values()):
    print(lang.title())
    
    
languages = {'python', 'ruby', 'python', 'c'}
print(languages)