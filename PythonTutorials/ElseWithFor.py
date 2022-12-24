menu = ['Bread', 'Rice', 'Milk']

for item in menu:
    print(item)

else:
    print('this for loop ended properly')

for item in menu:
    print(item)
    if item == 'Rice':
        break
else:
    print('this for loop ended properly')