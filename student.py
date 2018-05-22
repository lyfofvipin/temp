n = int(input("Enter number of student :: "))
nam = {}
for x in range(n):
    name = input("ENTER NAME OF STUDENT %d:: " % (x))
    nam[name] = 0
    marks = int(input("ENTER MARKS OF student in MATHEMATICS :: "))
    nam[name] += marks
    marks = int(input("ENTER MARKS OF student in PHYSICS :: "))
    nam[name] += marks
    marks = int(input("ENTER MARKS OF student in HISTORY :: "))
    nam[name] += marks
for x in nam:
    if nam[x] > 120:
        print("congrets %s you have passed your exames and your marks are %d :) " %(x,nam[x]))
    else:
        print("oops %s you fail in  youes exames and your marks are %d :( " %(x,nam[x]))