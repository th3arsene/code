a = 0
b = 0
c = 0
d = 0
g = False
aFinal = "You're just a normie. die :)"
bFinal = "What is life for you? Seek a therapist"
cFinal = "You're personality is bursting at the seams. Please don't kill me"
dFinal = "You're literally a corpse"
questions = ["What do you do in your free time? \n a: Talk to friends b: Tie a noose c: Stalk my crush d: Rot in the ground", ""]
for i in range(len(questions)):
    while g == False:
        g = True
        print(questions[i])
        ans = input("")
        if ans == "a":
            a +=1
        elif ans == "b":
            b+=1
        elif ans == "c":
            c+=1
        elif ans == "d":
            d+=1
        else:
            print("Invalid!")
            g = False
if a > b:
    if a > c:
        if a > d:
            print(aFinal)
        else:
            print(dFinal)
    else:
        if c > d:
            print(cFinal)
        else:
            print(dFinal)
else:
    if b > c:
        if b > d:
            print(bFinal)
        else:
            print(dFinal)
    else:
        if c > d:
            print(cFinal)
        else:
            print(dFinal)

