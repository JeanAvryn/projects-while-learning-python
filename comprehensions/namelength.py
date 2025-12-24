##ganito sya pag mahaba
names = ["Alice", "Bob", "Charlie"]
length = []
for name in names:
    length.append(len(name))
print(dict(zip(names,length)))

##ganito pag comprehended
names = ["Alice", "Bob", "Charlie"]
length = {name: len(name) for name in names}
print(length)
