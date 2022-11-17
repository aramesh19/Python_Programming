import math

sen1 = 'F String'
sen2 = 'Demo'

a = f'This is {sen1} {sen2}'
# print(a)

c = 'this is {0} {1}'
b = c.format(sen1, sen2)
print(b)

d = f'this is a math string of cos 30 {math.cos(30)}'
print(d)