#closures
# inner function that remembers and has access to the
# variables created in local scope
# even after the outer function has finished executing.
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func()
        # the message variable is a free variable, its not
        # its not created in the inner function.
outer_func() # this is a function call or execution

def ext_f():
    message = 'example2'
    def inter_f():
        print(message)
    return inter_f

var = ext_f() # var is assigned a function call which returns a function
# var is now a function
# that function is executed below.
print(var.__name__,": is the action function name")
var()

##############################################################

def out1(msg):
    message = msg
    def inner1():
        print(message)
    return inner1

hi_func = out1('Hi')
hello_func = out1('Hello')
hi_func()
hello_func()

###############################################

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

