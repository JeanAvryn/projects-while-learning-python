def shopping():
    basket = []
    
    while True:
        item = input("Add an item: ")
        numberOfItems = len(basket)
        
        if item == "done":
            print(f"You have {numberOfItems} items in your basket. They are {basket}.")
            break
        else:
            basket.append(item)
        
shopping()
        
