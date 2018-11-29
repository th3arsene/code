import collections
# Something stupid. oof
while True:
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
        print("The letter %s was in it %d times." % (key, value))
