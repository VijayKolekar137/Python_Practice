li_Num = []
num = 0

for i in range(4):
    num = int(input("Enter the number: "))
    li_Num.append(num)

# print(li_Num)

if(li_Num[0] > li_Num[1]):
    N1 = li_Num[0]
else:
    N1 = li_Num[1]

if(li_Num[2] > li_Num[3]):
    N2 = li_Num[2]
else:
    N2 = li_Num[3]

if(N1 > N2):
    print(str(N1) + " is greter")
else:
    print(str(N2) + " is greter")