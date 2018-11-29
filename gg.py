while True:
    yoted = input("Encode or Decode? e/d ")
    
    strs = 'abcdefghijklmnopqrstuvwxyz'      #use a string like this, instead of ord()
    data = []
    def shifttext(shift, yeet):
        inp = yeet
        for i in inp:                     #iterate over the text not some list
            if i.strip() and i in strs:                 # if the char is not a space ""  
                data.append(strs[(strs.index(i) + shift) % 26])    
            else:
                data.append(i)
    if (yoted == "d"):
        shifter = int(input("What to shift by? "))
        message = input("Input message to decode ")
        messagelist = list(message)
        for i in range (len(messagelist)):
            if messagelist[i] != "y" or messagelist[i] != "z":
                shifttext(shifter, str(messagelist[i]))
        message0 = ''.join(data)
        #message1 = message0.replace("y", "a")
        #message2 = message1.replace("z", "b")
        print(message0)
    elif (yoted == "e"):
        shifter = int(input("What to shift by? "))
        message = input("Input message to encode ")
        messagelist = list(message)
        for i in range (len(messagelist)):
            if messagelist[i] != "a" or messagelist[i] != "b":
                shifttext(-shifter, str(messagelist[i]))
        message0 = ''.join(data)
        #Wmessage1 = message0.replace("a", "y")
        #message2 = message1.replace("b", "z")
        print(message0)
    else:
        print("Invalid query")


