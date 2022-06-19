# For accepting the number input

age = input("How old are you? ")

print(age)
print(type(age))    # Data type is str

age = int(age)

print(type(age))    # Data type is converted to the int

# Example of int with the if-else

print("Example of int with the if-else")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enought to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")