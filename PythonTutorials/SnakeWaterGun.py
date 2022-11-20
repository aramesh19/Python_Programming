import random

l = ['S', 'W', 'G']
cc = 0
uc = 0
n = 1
eq = 0
while n <= 10:
    c = random.choice(l)
    u = input('Choose Snake-S, Water-W or Gun-G: ')
    n += 1
    if c == u:
        eq += 1
        print('your input and computer input are both same')
        continue
    elif c == 'S' and u == 'W':
        cc += 1
        print(f'Computer chose {c}, computer won')
    elif c == 'S' and u == 'G':
        uc += 1
        print(f'Computer chose {c}, you won')
    elif c == 'W' and u == 'S':
        uc += 1
        print(f'Computer chose {c}, you won')
    elif c == 'W' and u == 'G':
        cc += 1
        print(f'Computer chose {c}, computer won')
    elif c == 'G' and u == 'S':
        cc += 1
        print(f'Computer chose {c}, computer won')
    elif c == 'G' and u == 'W':
        uc += 1
        print(f'Computer chose {c}, you won')


print('The total times computer won: ', cc)
print('The total times user won: ', uc)
print('The number of times computer = User: ', eq)
if uc > cc:
    print('Out of 10 games, the user won the most: ', uc)
else:
    print('Out of 10 games, the computer won the most: ', cc)
