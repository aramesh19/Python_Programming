"""
Iterable-> __iter__() or __getitem__
Iterator-> __next__()
Iteration->
"""

# def gen(n):
#     for i in range(n):
#         yield i
#
#
# g=gen(10)
# print(g)
#
# g.__next__()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#
# var = 'Ramesh'
# i = iter(var)
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
####------------------------------------------------------
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result
#
# my_nums = square_numbers([1,2,3,4,5])
# print('\n')
# print(my_nums,end=" ")

### how to convert the above into a generator
# the presence of yeild keyword makes it a generator. it doesn't return the entire list
# instead the generator returns one result at a time. generators don't hold the entire result in memory
# generator waits for us to ask for the next result.
# Hence print(my_nums), doesn't give any output.
# __next__ needs to be used to get outputs from the generator
def squared(nums):
    for i in nums:
        yield(i*i)
my_nums = squared([1,2,3,4,5])
print(my_nums)
print(my_nums.__next__(), end=" ")
print(my_nums.__next__(), end=" ")
print(my_nums.__next__(), end=" ")
print(my_nums.__next__(), end=" ")
print(my_nums.__next__(), end=" ")
## print(my_nums.__next__(), end=" ") ## using this would throw an error "stopIteration".
# also, instead of using __next__ one at a time, a for loop can be used.
for en in my_nums:
    print(en,end=" ")