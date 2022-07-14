print("Enter the marks of seven student")

li_Marks = []
__intGB__ = 7

for i in range(__intGB__):
    m = input("Enter the marks of stuent: ")

    try:
        val = int(m)
        li_Marks.append(m)
        print(i)

    except ValueError:
        print("Enter the number")
        i = i - 1
        print(i)
       




print("Marks of seven student are : \n ", li_Marks)
