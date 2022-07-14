samDict = {}

for i in range(4):
    name = input("Enter your name: ")
    fav_sub = input("Enter your favorite subject: ")

    samDict.update({name:fav_sub})

print(samDict)
