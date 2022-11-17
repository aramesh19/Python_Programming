# Pattern printing

i = int(input('Enter a number: '))
pattern = int(input('Enter 1 or 0: '))

flag = bool(pattern)

if flag == True:
    for p in range(0,i+1):
        print('*' * p)
if flag == False:
    for p in range(i,0,-1):
        print('*' * p)


## -------------------------------------------


i1 = int(input('Enter a number: '))
p1 = int(input('Enter 1 for forward pattern and 0 for reverse: '))

flag = bool(p1)

if flag == True:
    for p in range(0, i1):
        for q in range(0, p+1):
            print('*', end='')
        print()
if flag == False:
    for p in range(i1, 0, -1):
        for q in range(1, p+1):
            print('*', end='')
        print()