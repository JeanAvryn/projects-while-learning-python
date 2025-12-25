transactions = [("Apple", 20), ("Banana", 15), ("Apple", 20), ("Orange", 25)]
def task1():
    print({item for item, price in transactions})
def task2():
    print([price + 5 for item, price in transactions])
def task3():
    print({item: price for item, price in transactions})
task1()
task2()
task3()
