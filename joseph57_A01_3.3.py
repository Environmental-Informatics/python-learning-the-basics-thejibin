## Spring-2020-ABE-65100
## Assignment 01
## Author: Jibin Joseph

## This function takes two arguments: a function object and value
## Calls the function twice by passing the value argument in the first funtion
## as the argument for the function called

def do_twice(arg1):
    arg1()
    arg1()

## This function takes one argument and calls another function twice
def do_four(arg2):
    do_twice(arg2)
    do_twice(arg2)

## This function takes three arguments, first argument - once,
## second argument - passed to perform 4 times
## third argument - once
def one_four_one(arg3, arg4, arg5):
    arg3()
    do_four(arg4)
    arg5()

## Displays + and output ends with space character
def disp_plus():
    print('+', end=' ')
## Displays - and output ends with space character
def disp_dash():
    print('-', end=' ')
## Displays | and output ends with space character
def disp_bar():
    print('|', end=' ')
## Displays o and output ends with space character
def disp_space():
    print('o', end=' ')
## This marks the end of the row
def disp_end():
    print("", end='\n')
## Dummy function
def empty():
    "Nothing executed"

## Tricky part - call multiple functions inside

def disp_1_beam():
    one_four_one(empty, disp_dash, disp_plus)

def disp_1_post():
    one_four_one(empty, disp_space, disp_bar)

def disp_4_beams():
    one_four_one(disp_plus, disp_1_beam, disp_end)

def disp_4_posts():
    one_four_one(disp_bar, disp_1_post, disp_end)

def disp_row():
    one_four_one(empty, disp_4_posts, disp_4_beams)

def disp_grid4x4():
    one_four_one(disp_4_beams, disp_row, empty)

disp_grid4x4()

