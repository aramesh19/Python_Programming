AY = input('Enter your age or year of birth: ')
YoB = 0
Age = 0
if len(AY) == 4:
    YoB = int(AY)
elif len(AY) == 3 and AY >= 100:
    print('you seem to be the oldest person alive')
elif len(AY) > 4:
    print('Enter a valid age or YoB')
elif AY == 0:
    print('you are not born yet')
elif (len(AY) == 1 and AY != 0) or len(AY) == 2:
    Age = int(AY)

if YoB != 0:
    when100 = YoB + 100
elif Age != 0:
    when100 = (2023-Age) + 100

YearofBirth = when100-100

print(f'You will be 100 by {when100}')

InterestedYear = int(input('Enter the year you want to know your age in: '))
print(f'you will be {InterestedYear - YearofBirth} years old in {InterestedYear}')
