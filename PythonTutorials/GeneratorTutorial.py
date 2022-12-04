"""
Iterable-> __iter__() or __getitem__
Iterator-> __next__()
Iteration->
"""

def gen(n):
    for i in range(n):
        yield i


g=gen(10)
print(g)

g.__next__()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

# var = 'Ramesh'
# i = iter(var)
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
