def add(x,y):
    return x + y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def user_input():
    while True:
        choice = input('Enter a number from 1 to 5 for operation: >> ')
        if choice in ['1', '2', '3', '4', '5']:
            print('You selected operation:', choice)
            return choice
        else:
            print('Invalid input, please try again.')
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

user_choice = user_input()
print(user_choice)