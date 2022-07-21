
# def fact_iter(n):
#     product = 1

#     for i in range(n):
#         product = product * (i+1)
#     return product

# print(fact_iter(4))

# Recursive function

num = int(input("Enter the number: "))



def fact_rec(n):
    if n == 1 or n == 0: 
        return 1
    elif n < 0:
        return ("Invalid input")
        
    return n * fact_rec(n-1)

print(fact_rec(num))
