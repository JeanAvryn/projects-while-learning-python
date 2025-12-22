def guessThePassword():
    
    secretkey = "Hello12345"
    
    while True:
        ask = input("Guess the password: ")
        
        if ask == secretkey:
            print("Access granted!")
            break
        
        else: 
            print("Wrong! Keep guessing.")
            
guessThePassword()
