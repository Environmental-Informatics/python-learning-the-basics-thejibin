## Spring-2020-ABE-65100
## Assignment 01
## Author: Jibin Joseph

## This function takes two arguments: a function object and value
## Calls the function twice by passing the value argument in the first funtion
## as the argument for the function called

def do_twice(arg_fun_obj, arg_val):
    #print ('1')
    arg_fun_obj(arg_val)
    #print ('2')
    arg_fun_obj(arg_val)
    #print ('3')

## This function prints the argument value twice
def print_twice(arg_val2):
    #print ('4')
    print(arg_val2)
    #print ('5')
    print(arg_val2)
    #print ('6')

#print ('7')
do_twice(print_twice, 'spam')
#print ('8')
