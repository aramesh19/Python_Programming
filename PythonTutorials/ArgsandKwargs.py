def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print('\nbelow is a kwargs list')
    for key, value in kwargs.items():
        print(f'special items are {key} and {value}')




arglist = ['a','b','c','d']
normal = 'following is a list'
kw = {'a':'1','b':'2','c':'3', 'd':'4'}

funargs(normal, *arglist, **kw)