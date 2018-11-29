import random
count = 0
f = open("highscore.txt", "r")
currentHigh = int(f.read())
f.close()
guessed = False
print("The current high score is: {}".format(currentHigh))
difficulty = int(input("What do you want the difficulty to be (Number)"))
guessNumber = random.randint(0,difficulty+1)
while (guessed == False):
    guess = int(input("What's your guess \n"))
    count += 1
    if (guess == guessNumber):
        guessed = True
    elif (guess < guessNumber):
        print("Higher")
    elif (guess > guessNumber):
        print("Lower")
    elif(count == "50"):
        break
if(count != 50):
    print("congrats!")
    if((50 - count) * difficulty > currentHigh):
        f = open("highscore.txt", "w")
        f.write(str((50 - count) * difficulty))
        f.close()
        print("You got a new high score of {}!".format((50-count)*difficulty))

else:
    print("You lost...")
    f = open("highscore.txt", "w")
    f.write(str(currentHigh))
    f.close()
