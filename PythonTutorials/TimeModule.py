import time
print('Seconds elapsed since 1-Jan-1970 (epoch): ', time.time())

#localtime
print(time.asctime())

print(time.localtime())


initial = time.time()
k=0
while k<45:
    print('we are in while loop')
    k+=1
print('this while loop ran for: ',time.time()-initial,'seconds')

initial2 = time.time()
for i in range(45):
    print('we are in for loop')
print('this while loop ran for: ',time.time()-initial2,'seconds')

localtime = time.asctime(time.localtime(time.time()))
print(localtime)