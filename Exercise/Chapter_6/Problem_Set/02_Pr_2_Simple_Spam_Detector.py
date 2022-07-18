sample_input = input("Enter the text here: ")

if("make money" in sample_input):
    spam = True
elif("buy now" in sample_input):
    spam = True
elif("Subcribe this" in sample_input):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")