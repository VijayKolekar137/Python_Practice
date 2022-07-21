# Recursive fuction to print the sum of first N natural number

def Sum_N(Num):
    if Num == 1:
        return 1
    return Num + Sum_N(Num - 1)

print(Sum_N(4))

