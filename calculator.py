def calculator():
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operations = ["+", "-", "*", "/"]

    oper = input(f"Select an operation {operations}: ")
        
    if oper == "+":
        print(f"The result of {num1} + {num2} = {num1 + num2}.")
    elif oper == "-":
        print(f"The result of {num1} - {num2} = {num1 - num2}.")
    elif oper == "*":
        print(f"The result of {num1} * {num2} = {num1 * num2}.")
    elif oper == "/":
        if oper != 0:
            print(f"The result of {num1} / {num2} = {num1 / num2}.")
        elif oper == 0:
            print("You dumbo, you cannot divide by zero.")
    
    
calculator()
            
