def avg_func(a,b):
    """ This is a docstring that explains that this is a function which will calculate average of two numbers"""
    return (a+b)/2

v = avg_func(7,19)
print(v)

print(avg_func.__doc__)

print('Enter a number')
n1 = input()
print('Enter another number')
n2 = input()
try:
    print('the sum is: ', int(n1)+int(n2))
except Exception as e:
    print(e)