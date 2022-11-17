l=10

def func1():
    #l=5 #local
    m=8 #local
    global l
    l=l+45
    print(l,m)

print(func1())

x=89
def func2():
    x=20
    def func3():
        global x
        x=88
    print('before calling func3()',x)
    func3()
    print('after calling func3()',x)

func2()
print(x)