def passwordCounter():
    
    while True:
        password = input("Enter new password:  ")
    
        counter = len(password)
        if counter < 8:
            print("Weak password!")
        elif counter >= 8:
            print("Got it!")
            break
        
passwordCounter()
