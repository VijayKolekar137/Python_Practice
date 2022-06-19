# A list of dictinories

alien_0 = {'color': 'green', 'points' : 5}
alien_1 = {'color': 'yellow', 'points' : 10}
alien_2 = {'color': 'red', 'points' : 15}

aliens = [alien_0,alien_1,alien_2]

for al in aliens:
    print(al)
    
    
# Make 30 green alien

# Empty list

li_al = []

for al_number in range(30):
    new_al = {'color' : 'green', 'points' : 5 , 'speed' : 'slow'}
    li_al.append(new_al)
    
    
    
print('\n30 alines ')

for ali in li_al[:5]:
    print(ali)
    

print(f'Total numbers of alines: {len(li_al)}')



for a in li_al[:3]:
    if a['color'] == 'green':
        a['color'] = 'yellow'
        a['speed'] = 'medium'
        a['points'] = 10
        
        
# Show first 5 aliens

for alia in li_al[:5]:
    print(alia)
    
    
print('........')
  
  

# A list in a dictionary

print('\n-------------\nA list in a dictionary')

# Store information about a pizza being ordered

print('Store information about a pizza being ordered')

pizza = {
            'crust' : 'thick',
            'toppings' : ['mushrooms','extra cheese'],
            }
            
# Summarize the order.

print(f"Your ordered a {pizza['crust']} - crust pizza"
        " with the following toppings")
        
        
for toppings in pizza['toppings']:
    print("\t" + toppings)

            
            
