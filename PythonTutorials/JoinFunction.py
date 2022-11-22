lis = ['London', 'Melbourne', 'Atlanta', 'Paris', 'NewYork', 'NewDelhi', 'Boston']

for item in lis:
    print(item, ' and ',end = ' ')

a = ' and '.join(lis)
print('\n',a, ' are the major cities of the world')

b = ', '.join(lis)
print(b, 'are the major cities of the world')