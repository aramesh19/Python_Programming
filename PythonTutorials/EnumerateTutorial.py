l1 = ['India','Mexico', 'Brazil','Russia','China','SouthAfrica']
i=0
for item in l1:
    if (i % 2) == 0:
        print(i, item)
    i+=1

print('\n')

for index, item in enumerate(l1):
    if (index % 2) == 0:
        print(index, item)