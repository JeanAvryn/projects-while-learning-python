def decimalCode():
    print('BINARY TO DECIMAL!')
    number = input('Enter a binary code: ')
    firstInput = number
    total = 0
    # Multiply each character of the binary code by 2 ** its ascending character.
    # e.g. 1101 = (1*(2^3)) + (1*(2^2)) + (0*(2^1)) + (1*(2^0))
    # 1 1 0 1
    #       firstInput[-1**()]
    newCode = (firstInput[::-1])
    for i, digit in enumerate(newCode):
        factors = int(digit) * int(2**i)
        total += factors
    return f"The decimal of {number} is {total}."
    
def binaryCode():
    print('DECIMAL TO BINARY!')
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

def main():
    print('Select if u want to convert decimal to binary or binary to decimal!')
    ask = int(input('[1] Binary to Decimal.\n[2] Decimal to Binary.\nI CHOOSE: '))
    if ask == 1:
        print(decimalCode())
    elif ask == 2:
        print(binaryCode())
    while ask not in [1,2]:
        print('lol')
        break
main()
    
