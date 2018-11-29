g = False
while (g == False):
    i = 0
    h = 0
    l = 0
    i = int(input("number 1: "))
    h = i
    l = i
    for b in range(9):
        i = int(input("number {}: ".format(b + 2)))
        if (i > h):
            h = i
        elif (l > i):
            l = i
    print("The highest is {}, and the lowest is {}".format(h, l))
j = input("repeat? y/n")
    if (j == "n"):
        g = True
