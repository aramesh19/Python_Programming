dic = {}
print(type(dic))
dic = {'india': 'delhi', 'Aus': 'sydney', 'Ukraine': 'Kyiv',
       'US': {'East': 'Atlanta', 'midwest': 'chicago', 'Mountain': 'Colorado'}}
print(dic['india'])
print(dic['US'])
print(dic['US']['East'])
print('\n the values of a dictionary can be a tuple, list or another dictionary')
dic['UK'] = 'London'
dic.update({'Thailand': 'Bangkok'})
print('\n', dic)
del dic['UK']
print('\n', dic)
d2 = dic.copy()
print("this is copied dic:\n", d2)
print('\n', d2.keys())
print('\n', d2.items())
print(dic['india'])

d1 = {'R': 1, 'S': 2, 'T': 3, 'U': 4, 'V': 5}
Key = input('enter a key to get a value: ')
print(d1[Key])
