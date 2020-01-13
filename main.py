import math

def addFoo(x,y):
    return(x+y)

def subFoo(x,y):
    return(x-y)

def multFoo(x,y):
    return(x*y)

def divFoo(x,y):
    return(x,y)

operationInput = int(input("Select an operation...\n1. Add\n2. Sub\n3. Mult\n4. Div\n5. Raise to a power\n6. Square root\nInput: "))

if(operationInput in range(1,7)):
        firstNumber = int(input("Please enter your first number: "))
       
        if(operationInput == 6):
            print("Skipping... No second number needed.")
            print("The square root of ", firstNumber, " is ",  math.sqrt(firstNumber))
        else:
            secondNumber = int(input("Please enter your second number: "))
            if(operationInput == 1):
                print(firstNumber, " + ", secondNumber, " = ", addFoo(firstNumber, secondNumber))

            elif(operationInput == 2):
                print(firstNumber, " - ", secondNumber, " = ", subFoo(firstNumber, secondNumber))

            elif(operationInput == 3):
                print(firstNumber, " * ", secondNumber, " = ", multFoo(firstNumber, secondNumber))

            elif(operationInput == 4):
                print(firstNumber, " / ", secondNumber, " = ", divFoo(firstNumber, secondNumber))

            elif(operationInput == 5):
                print(firstNumber, "^", secondNumber, " = ", math.pow(firstNumber, secondNumber))
            
else:
    print("Incorrect input")
