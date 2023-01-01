def square(x):
    return x * x

def cube(x):
    return x * x * x

f = square(5)
print(square)
print(f)

g = square
print(g(5))
## assigning the RESULT of a function to a variable is different from assigning the function to a variable.
# we pass functions as arguments and return functions as results. functions which do this are called higher order functions

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
squares = my_map(cube, [1,2,3,4,5])
print(squares)

# Return a function as a result.
def logger(msg):
    def log_message():
        print("log:", msg)
    return log_message

log_hi = logger('Hi!')
# the below log_hi variable can be treated as a function because this variable is
## assigned a function. Hence the Parenthesis during the call.
log_hi()

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

h1 = html_tag('h1')
h1('headline1')
h1('headline2')

p = html_tag('p')
p('Paragraph')

h1 = html_tag('h2')
h1('NewHeadline')

