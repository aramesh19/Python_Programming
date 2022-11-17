R = 19
guess = 5

while (guess > 0):
    i = int(input('\n Enter a number:'))
    if (i < R) and guess != 0:
        print('Your value is smaller, try again')
        guess = guess - 1
        print('no. of guess left:', guess)
        continue
    elif i > R and guess != 0:
        print('Your value is larger, try again')
        guess = guess - 1
        print('no. of guess left:', guess)
        continue
    elif i == R  and guess != 0:
        print('\n Congrats your value matches')
        print('\n Number of guesses took', guess)
        break


if (guess == 0):
    print('\n Game Over')


# R=19



