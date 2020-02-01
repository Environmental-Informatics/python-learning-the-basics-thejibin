"""Created on 2020-01-24
by Jibin Joseph

Assignment 01: Python - Learning the Basics
Think Python Chapter 3: Exercises 3.2

Use the modified version of do_twice to call print_twice twice,
passing 'spam' as an argument.

Modified to add comments
"""


"""
This function takes two arguments: a function object and value
Calls the function twice by passing the value argument in the first funtion
as the argument for the function called
"""

def do_twice(arg_fun_obj, arg_val):
    arg_fun_obj(arg_val)
    arg_fun_obj(arg_val)

"""
This function prints the argument value twice
"""

def print_twice(arg_val2):
    print(arg_val2)
    print(arg_val2)

## Main code
do_twice(print_twice, 'spam')
