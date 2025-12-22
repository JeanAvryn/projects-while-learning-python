#ATM

def atm():
    balance = 1000
    while True:
        process = int(input("What do you want to do? \n1. Withdraw\n2. Deposit\n3. Exit\n I want to: "))
        print()
        if process == 1:
            withdraw = int(input("How much do you want to withdraw: "))
            if withdraw > balance:
                print("Insuffienct funds.")
            elif withdraw <= balance:
                balance -= withdraw
        elif process == 2:
            deposit = int(input("How much do you want to deposit: "))
            balance += deposit
            print(f"Your balance is now {balance}")
        elif process == 3:
            break
atm()
