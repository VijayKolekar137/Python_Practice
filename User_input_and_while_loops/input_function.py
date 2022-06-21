# Now we check how the input function works

message = input("Tell me something about you.")

print(message)


name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Personalize the input

promt = "If you tell us who you are we can personalize the messages you see."
promt += "\nWhat is your first name? "

name = input(promt)

print(f"\nHello, {name} !")
