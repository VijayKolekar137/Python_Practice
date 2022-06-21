promt = "\nTell me something, and I will reperat it back to you: "
promt += "\nEnter 'quit' to end the program."

message = ""

while message != 'quit':
    message = input(promt)

    if message != 'quit':
        print(message)