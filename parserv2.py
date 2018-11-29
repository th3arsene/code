import collections
import sys
# Something stupid. oof
# by HaloMC6#7106
something = input("Would you like to sort by number, or letter? (n/l) ")
if (something == 'n'):
    print("Showing by number!")
elif (something == 'l'):
    print("Showing by letter!")
while True:
    error = False
    count = 0
    if (something == 'l'):
        parseMe = str(input("Enter Text to parse: ")).lower()
        words = list(parseMe)
        counter = collections.Counter(words)
        # print(words)
        values = list(counter.values())
        keys = list(counter.keys())
        dictionary = dict(zip(keys, values))
        sorted_by_value =list(sorted(keys))
        #print (sorted_by_value)
        for i in range(0, int(len(values))):
            key = sorted_by_value[i]
            value = dictionary[sorted_by_value[i]]
            count = count + value
            print("The letter %s was in it %d times." % (key, value))
        if (count == 1):
            print("In total, there was", count, "character in your text.")
        else:
            print("In total, there were", count, "characters in your text.")
    elif (something == 'n'):
        parseMe = str(input("Enter Text to parse: ")).lower()
        words = list(parseMe)
        counter = collections.Counter(words)
        # print(words)
        values = list(counter.values())
        keys = list(counter.keys())
        dictionary = dict(zip(keys, values))
        sorted_by_value = sorted(dictionary, key=dictionary.get)
        #print (sorted_by_value)
        for i in range(0, int(len(values))):
            key = sorted_by_value[i]
            value = dictionary[sorted_by_value[i]]
            count = count + value
            print("The letter %s was in it %d times." % (key, value))
        if (count == 1):
            print("In total, there was", count, "character in your text.")
        else:
            print("In total, there were", count, "characters in your text.")
    else:
        print("Invalid!")
        error = True
        something = input("Would you like to sort by number, or letter? (n/l) ")
    if (error == False):
        something2 = input("Would you like to quit, change mode, or go again? (q, c, a)")
        if (something2 == 'q'):
            sys.exit()
        elif (something2 == 'c'):
            if (something == 'n'):
                something = 'l'
                print("Showing by letter!")
            elif (something == 'l'):
                something = 'n'
                print("Showing by number!")
                
                
    
    
        
