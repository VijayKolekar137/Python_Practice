# Even or odd 

number = input("Enter a number and I will tell you it is even or odd : ")
number = int(number)

if number >= 0:
    if number == 0:
        print("Number is zero it is neither even nor odd") 
    
    else:
        if number % 2 == 0: 
            print(f"\nThe number {number} is even.")
        else:
            print(f"\nThe number {number} is odd.")
else:
    print("Enter the valid number.")