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
def dec1(func1):
    def nowexec():
        print('begin execution')
        func1()
        print('Executed')
    return nowexec

# instead of explicitly writing another_func = dec1(another_func) just write @dec1 above the function declaration.
@dec1
def another_func():
    print('this is another function')

## change the function behavior
#another_func = dec1(another_func)
# another way of writing the above line is by mentioning @dec1 above the function.

## executing the function
another_func()


