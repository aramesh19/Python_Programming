import random
r = random.randint(0,5)
print('random.randint between 0 & 5: ', r)
r2 = random.random()
print('random.random between 0 & 1: ', r2)
print('random.random between 0 & 100: ', r2*100)
r3 = random.uniform(10,25)
print('random.uniform: ',r3)

l = ['a','b','c','d','e','f']
c=random.choice(l)
print('random.choice: ',c)
