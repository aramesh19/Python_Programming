print('Input the number of apples, Min and Max students')
N = int(input('Enter the number of apples: '))
Min = int(input('Enter the MINIMUM number of students: '))
Max = int(input('Enter the MAXIMUM number of students: '))

if Min == Max or Min > Max:
    print('Minimum students cannot be equal or greater than Max students')

for i in range(Min, Max+1):
    if N % i == 0:
        print(f'{i} is a divisor of {N}')
    else:
        print(f'{i} is not a divisor of {N}')
