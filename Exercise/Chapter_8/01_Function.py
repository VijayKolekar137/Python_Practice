marks = 0
sub = 6
marks_Li = []

def Enter_Mark(sub):
    for i in range(sub):
        marks = int(input(("Enter the marks of the each subject: ")))
        marks_Li.append(marks)
    Print_Li()

def Print_Li():
    for item in marks_Li:
        print(item)


Enter_Mark(sub)


