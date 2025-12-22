def numberGuesser():
    import random
    
    system = random.randint(1, 20)
    
    while True:
        guess = int(input("Guess a number: "))
        if guess > system:
            print("Lower!")
        elif guess < system:
            print("Higher!")
        elif guess == system:
            print("Nice!")
            break
            
numberGuesser()
