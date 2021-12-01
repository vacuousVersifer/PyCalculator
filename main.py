def getNumber(num):
    print("Enter number ", num, ": ", sep="", end="")
    return float(input())

def getOperand():
    return input("Enter the operand: (+, -, *, /, or %) ")

def start():
    operand = getOperand()
    num1 = getNumber(1)
    num2 = getNumber(2)

    result = 0

    if operand == "+":
        result = num1 + num2
    elif operand == "-":
       result = num1 - num2
    elif operand == "*":
       result = num1 * num2
    elif operand == "/":
     result = num1 / num2
    elif operand == "%":
       result = num1 % num2
    else:
        print("That's not an operation! Try again.")
        start()

    print(result)
        

print("Welcome to my calculator!")
start()