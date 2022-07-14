# Finding the meaning of word from the dictionary

samDict = {
    "Khurchi" : "Chair",
    "Vati" : "Bowl",
    "Dabba" : "BOx"
}

print("Options are", samDict.keys())
word = input("Enter the word from above list: ")

print("Meaning of the your word is",samDict.get(word))

