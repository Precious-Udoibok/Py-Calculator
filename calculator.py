#Python Calculator
#importing the logo
from art import logo
#Functions to peform the operations.
def add(n,m):
    return n + m

def subtract(n,m):
    return n - m

def divide(n,m):
    return n / m

def multiply(n,m):
    return n * m

#create a dictionary for the operations
operations = {}
operations['+'] = add
operations['-'] = subtract
operations['/'] = divide
operations['*'] = multiply

#recursion
#define a function to perform the recursion
def calculator():
    print('\nWecome to the Py Calculator')
    print(logo) #dispay the logo
    num1 = float(input('What\'s the first number: ')) #get the user first number
    #loop through the dict
    for signs in operations:
        print(signs) #display the keys

    # a flag to continue calculating
    continue1 = True 
    while continue1:
        operations_symbols = input('Enter an operation: ') #ask the user to enter an operation
        num2 = float(input('What\'s the next number: ')) #ask the user for the  next operation
        calc_func = operations[operations_symbols] #gets the functions in the dict and store it in a variable
        #calling the function and passig the user inputs and store it in a variabe
        result1 = calc_func(num1,num2) 
        print(f'{num1} {operations_symbols} {num2} = {result1}')

        calculating = input(f'Type y to continue calculating with {result1} or type n to start a new calculation: ').lower()
        if calculating == 'y':
            num1 = result1 # set the num1 to the current result
        else: #if no
            continue1 = False #ends the while loop
            calculator() #this is recursion, call the function in the function to start the caculator again.
calculator() #call the function