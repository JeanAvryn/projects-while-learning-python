def binaryCode():
    firstNumber = int(input('Enter a number: '))
    quotient = firstNumber
    binary = []
    
# Binary process: divide the number by 2 until it's 0r.1, then list the remainders in reverse.

    while quotient > 0:
        remainder = quotient % 2
        quotient = quotient // 2
        binary.append(remainder)
    
    string = map(str, binary[::-1])
    code = "".join(string)
    return f"The binary code of {firstNumber} is {code}."

print(binaryCode())
        
        
