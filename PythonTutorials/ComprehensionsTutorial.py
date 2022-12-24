ls = []
for i in range(100):
    if i%3 == 0:
        ls.append(i)

#print(ls)

# List comprehensions

l2 = [i for i in range(100) if i%3==0]
#print(l2)


dic1 = {i:f'item {i}' for i in range(50) if i %10==0}
print(dic1)
dic1 = {i:f'item {i}' for i in range(50) }
dic2 = {value:key for key, value in dic1.items() if key%10==0}
print(dic2)

#set comprehension unlike list comprehension returns only the unique items
set_of_words = {word for word in ['a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d']}
print(set_of_words)

# Generator comprehension
evens = (i for i in range(25) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print('two are printed')
for item in evens:
    print(item)

