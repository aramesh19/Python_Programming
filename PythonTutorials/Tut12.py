v1 = int(input('Enter your first number:'))
v2 = int(input('Enter your second number:'))
opr = input('Enter the operand:')

if opr == '+':
    if (v1 == 56 and v2 == 9) or (v1 == 9 and v2 == 56):
        ans = 77
    else:
        ans = v1 + v2
elif opr == '-':
    ans = v1 - v2
elif opr == '*':
    if (v1 == 45 and v2 == 3) or (v1 == 3 and v2 == 45):
        ans = 555
    else:
        ans = v1 * v2
elif opr == '/':
    if v1 == 56 and v2 == 6:
        ans = 4
    else:
        ans = v1 / v2
print(ans)
