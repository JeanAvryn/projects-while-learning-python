## this is pag for loop right?

data = [10, -5, 30, -2, 50, 8]
positive = []
for data in data:
    if data > 0:
        positive.append(data)
    else:
        positive.append(0)
print(positive)



## and this is pag list comprehension

data = [10, -5, 30, -2, 50, 8]
positive = [number if number > 0 else 0 for number in data]
print(positive)
