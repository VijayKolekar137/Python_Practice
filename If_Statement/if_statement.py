# Simple example of if statement

cars = ['audi', 'bmw', 'subaru', 'toyota']

for c in cars:
	if c == 'bmw':
		print(c.upper())
	else:
		print(c.title())


# Conditional Tests

print('\n Checking for equality')

car = 'bmw'

print(car == 'bmw')

car = 'Audi'

print(car == 'bmw')

print(car.lower() == 'audi')

print(car)


# Checking for inequality

print('\nChecking for inequality')

req_top = 'mushrooms'

if req_top == 'anchovies':
	print('Hold the achovies!')
else:
	print('Hold the mushrooms')


# Numerical Comparison

print('\nNumerical Comparison')

age = 18

print(age == 18)

print('\nExample 2')

ans = 17

if ans != 42:
	print('That is not the correct answer, please try again!')

# Checking wheter a value is not in a list

print('\nChecking wheter a value is not in a list\n')

ban_users = ['andrew','carolina','david']
user = 'marie'

print(ban_users)

if user not in ban_users:
	print(f"{user.title()}, you can post a response if you wish.")

# if-else statement:

print('\n if-else statement\n')

age = 18

if age >= 18:
	print('You are old enough to vote!\nHave you registered to vote yet?')
else:
	print('Sorry, you are too young to vote')

# Checking for special items

print('\nChecking for special items\n')

req_top = ['mashrooms','green peppers', 'extra cheese']

for rp in req_top:
	print(f"Adding {rp}.")

print('\nFinised making your pizza!')

# Using multiple lists

print('\nUsing multiple lists\n')

avi_top = ['mushrooms','olives','green pepprs',
	'pepperoni', 'pineapple','extra chhese']

req_top = ['mushrooms','french fires','extra cheese']

print(req_top)

for rq in req_top:
	if rq in avi_top:
		print(f"Adding {rq}.")
	else:
		print(f"Sorry, we don't have {rq}.")

print("\nFinised making your pizza!\n")


 


