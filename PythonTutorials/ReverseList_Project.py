L=[]
n = int(input('Enter the size of the list: '))
for i in range(0,n):
    ele = int(input('Enter an element: '))
    L.append(ele)

print(L)
L.reverse()
print('using Reverse function',L)

#Resetting
L = list(reversed(L))

def reverse_slicing(Lst):
    rev_list = Lst[::-1]
    return rev_list

RL_slicing = reverse_slicing(L)
print('Reversed list using slicing: ',RL_slicing)

def ReverseTech(Lst):
    first = 0
    last = len(Lst)-1
    while first < last:
        temp = Lst[first]
        Lst[first] = Lst[last]
        Lst[last] = temp
        first += 1
        last -= 1
    return Lst

print('Reversed List using manual reversing: ', ReverseTech(L))