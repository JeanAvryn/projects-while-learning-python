first = [1, 2, 2, 3, 4, 4, 4, 5]
second = []

for num in first:
    if num not in second:
        second.append(num)
print(second)
