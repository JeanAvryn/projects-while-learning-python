def absent():
    keyword = '1234567890abcdefghijklmnopqrstuvwxyz'
    word = input('Enter word: ')
    newlist = []
    for char in keyword:
        if char.lower() not in word:
            newlist.append(char.lower())
    print(''.join(newlist))
absent()
