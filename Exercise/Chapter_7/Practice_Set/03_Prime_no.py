num = int(input("Enter the number: "))

prime_f = True

if(num > 1):
    for i in range(2,num):

        if(num%i == 0):
            prime_f = False
            break

    if prime_f:
        print("Number is prime")
    else:
        print("Number is not prime")