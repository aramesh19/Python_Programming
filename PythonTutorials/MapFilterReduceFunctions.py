integers = ['5','37','7','19']

for item in range(len(integers)):
    integers[item] = int(integers[item])

integers[2] = integers[2]+2
print(integers)

## using map method. for the first parameter should be
# the function that needs to be applied across all elements
# the second parameter is the list or data against which the function needs to be applied.
numbers = ['7', '19', '5', '37']
numbers = list(map(int, numbers))

numbers[0] = numbers[0]-4
print(numbers)

def sq(b):
    return b*b

num = [4,2,5,34,66,7,19]
square = list(map(sq,num))
print(square)
## using a lambda function with in a map.
sq_lambda = list(map(lambda c:c*c,num))
print(sq_lambda)

def cube(c):
    return c*c*c

func = [sq,cube]

for i in range(6):
    val = list(map(lambda f:f(i),func))
    print(val)

#------------------------------------------------------------------
#------------------------------------------------------------------
## Filter Function:
l1 = [1,2,3,4,5,6,7,8,9,10]
def isgreater7(num):
    return num>7

greater_7 = list(filter(isgreater7, l1))
print('\nFollowing numbers are greater than 7: ',greater_7)

#------------------------------------------------------------------
#------------------------------------------------------------------
## Reduce Function:
from functools import reduce
l2 = [10,2,10,3,10,4]
reduce_num = reduce(lambda x,y:x+y,l2)
print("this is the output of reduce : ",reduce_num)

