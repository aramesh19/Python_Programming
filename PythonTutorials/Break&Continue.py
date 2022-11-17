i=0

while i<45:
    print(i)
    if i==44:
        break
    i+=1

print("\n while loop using P")
p=0
while(p<45):
    if p < 5:
        p += 1
        continue
    print(p, end=" ")

    if p == 44:
        break
    p += 1

print('\npop quiz')

v=0
while v <= 100:
    v = int(input('Enter a numeric value:'))
    if v < 100:
        continue
    if v > 100:
        print('good you entered a value greater than 100')
        break

