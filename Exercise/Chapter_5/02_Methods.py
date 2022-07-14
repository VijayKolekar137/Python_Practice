sam_dict = {
    "Name": "Vijay",
    "Hobi" : ["Movies","Suffering","Listing Songs"],
    "Marks" : [45,96,78],
    "anotherdict" : {"Friends" : "No"},
}

print(sam_dict.keys())      #Prints the keys of the dictionary
print(sam_dict.values())    #Print the values of the dictionary
print(sam_dict.items())     #Prints the items from the dictionary

update_dict = {
    "Name": "Rahul",
    "Hobi" : ["Movies","Suffering","Listing Songs"],
    "Marks" : [45,96,78],
    "anotherdict" : {"Friends" : "No"},
}

sam_dict.update(update_dict)    #Update the dictionary by adding key-value pairs from update_dict
print(sam_dict)

# Difference between .get() method and [] 
print(sam_dict.get("Name1"))    # It gives output as none
# print(sam_dict["Name1"])      # It throws the error