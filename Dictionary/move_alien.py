
# Moving the position of aline

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}

x_increment = 0

speed_limit = eval(input('Choose the speed limit of aline'))

if speed_limit == 1:
    alien_0['speed'] = 'slow'
    x_increment = 1
elif speed_limit == 2:
    alien_0['speed'] = 'medium'
    x_increment = 2
elif speed_limit == 3:
    alien_0['speed'] = 'fast'
    x_increment = 3
else:
    print('Invalid speed')





    

print(f"Original position : {alien_0['x_position']}")

# The new position if the old position plue the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")