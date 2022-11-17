L = ['Youngkin', 'DeSantis', 'Lake', 'Huckabee', 'Kemp', 'Fetterman']

for item in L:
    print(item)

T = ('Youngkin', 'DeSantis', 'Lake', 'Huckabee', 'Kemp', 'Fetterman')

for item in T:
    print('\t', item)

LL = [['Youngkin', 'Virginia'],
      ['DeSantis', 'Florida'],
      ['Lake','Arizona'],
      ['Huckabee', 'Arkansas'],
      ['Kemp','Georgia'],
      ['Fetterman','Pennsylvania']]

for item, ff in LL:
    print(item,' and state is : ',ff)

D1 = dict(LL)
print(D1)

for item in D1:
    print(item)


List1 = ['Youngkin', 'DeSantis', 'Lake', 'Huckabee', 'Kemp', 'Fetterman',1,2,10,11]
print('\nNew Exercise')

for item in List1:
    if str(item).isnumeric() and item > 6:
        print(item)


i=0

while i<45:
    print(i)
    i+=1