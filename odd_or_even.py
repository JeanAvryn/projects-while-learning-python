def odd_or_even():
    number = input("Enter a number: ")
    try:
        numbers = int(number)
        
        if numbers % 2 == 0:
            print(f"Your number {numbers} is even. ")
        elif numbers % 2 != 0:
            print(f"Your number {numbers} is odd.")
    except ValueError:
        print("Select a new number: ")
        
odd_or_even()
