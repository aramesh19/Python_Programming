a = input('what is your name : ')
b = input('how much do you earn : ')
if int(b) == 0:
    raise ZeroDivisionError('Earning cannot be zero')

if a.isnumeric():
    raise Exception('No Numbers please')

print(f'Hello {a}')

a = [6,4,'ab']
b = [6,4,'ab']
print(b is a)
print(b == a)
c=a
print('c = ',c)
c[0] = 10
print('c = ',c)
print('a = ',a)