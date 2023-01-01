# A decorator is a function that takes
# another function as an argument and adds some functionality
# and then returns another function.
# without altering the code of the original function
# that was passed in

# def function1():
#     print('this is function1')
#
# func2 = function1
# del function1
# func2()

## A function can be returned by/from another function.
# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
# a = funcret(1)
# print(a)

## take function as an input and execute it inside the function
# def executor(infunc):
#     infunc('this is infunc, printed via "executor" ')
#
# executor(print)

##----------------------DECORATORS-------------------------
## take a function as an input parameter, the body has another function. and then return the function
# def dec1(func1):
#     def nowexec():
#         print('begin execution')
#         func1()
#         print('Executed')
#     return nowexec

# instead of explicitly writing another_func = dec1(another_func) just write @dec1 above the function declaration.
# @dec1
# def another_func():
#     print('this is another function')

## change the function behavior
#another_func = dec1(another_func)
# another way of writing the above line is by mentioning @dec1 above the function.

## executing the function
#another_func()
#############################################################

# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function
# # returns a wrapper function that is waiting to be executed
#
# def display():
#     print('display function ran')
#
# decorated_display = decorator_function(display)
# decorated_display()
########*************&&&&&&&&&&&&&&&&&&&&&&&*********************

# def decorator_function(original_function):
#     def wrapper_function():
#         print('\nNow using @decorator')
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function
#
# @decorator_function
# def display():
#     print('display function ran')
# display()

###############################################################

# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

display_info('John', 25)

import time
@my_timer
def display(name, age):
    time.sleep(2)
    print('display rain with arguments ({},{})'.format(name, age))

display('Hank',30)

