grocery = ['harpic','vim bar','deodrant','bhindi','5star',56]
print(grocery)
print(grocery[1:3])
numbers = [2,7,9,11,3]
print(numbers[1])
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers = [12,13,111,1,10,7]
numbers.insert(3,37)
print(numbers)
numbers.remove(37)
print(numbers)
numbers.pop()
print(numbers)

numbers[1] = 5
print(numbers)
print("\nitems in a list can be changed, the same cannot be done in tuples")

tp =(37,5,19,7)
print('\nTuple')
print(tp)

a=1
b=8
print('\n',a,b)
print("Swap a and b")
a,b=b,a
print("\n",a,b)