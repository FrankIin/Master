def add(x,y):
    return x + y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def user_input(action = 'select_operation'):
    if action == 'select_operation':
        while True:
            choice = input('Enter a number from 1 to 5 for operation: >> \n1: Add\n2: Substract\n3: Multiply\n4: Divide\n5: Exit\n')
            if choice in ['1', '2', '3', '4', '5']:
                print('You selected operation:', choice)
                return choice
            else:
                print('Invalid input, please try again.')
    else:
        while True:
            try:
                choice = int(input(f'Enter a {action} number for the operation: >>'))
                return choice
            except:
                print('Invalid input, please try again.')

def select_operation(number):
    operations = [add, substract, multiply, divide]
    if number == '5':
        print('Exiting the calculator. Goodbye!')
        return
    else:
        return operations[int(number)-1](user_input('first'),user_input('second'))  
    # checks if the number is between 1 and 5 to select a operation

print(select_operation(user_input()))