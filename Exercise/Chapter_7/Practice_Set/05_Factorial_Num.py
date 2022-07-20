num = int(input("Enter the numebr: "))
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print(f"Factorial of {num} is {fact}")
