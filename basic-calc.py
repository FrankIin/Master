def add(x,y):
    return x + y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def user_input():
    # ask user input
    # checks if it is a number
    pass

def select_operation(number):
    num1 = 1
    num2 = 2
    operations = [add, substract, multiply, divide]
    return operations[number-1](num1,num2)
    # checks if the number is between 1 and 5 to select a operation


    pass

'''
Weclome to the calculator!
Press for operation:
1: Add
2: Substract
3: Multiply
4: Divide
5: Exit
'''