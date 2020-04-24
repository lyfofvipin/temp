with open("./log.log") as file:
    a = []
    for line in file.readlines():
        if "log size" in line:
            a.append(int(line.split()[-1]))
    print(a)
    print(max(a))