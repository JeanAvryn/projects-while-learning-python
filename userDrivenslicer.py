def getCustom():
    word = input("ENTER A WORD: ")
    number = input("ENTER A NUMBER: ")
    number = int(number)
    
    newWord = word[-number:]
    return newWord

print(getCustom())
