f1 = open('text2')

try:
    f1 = open('text3')
except Exception as e:
    print(e)
else:
    print('this will run if except is not running')
finally:
    print('Run this anyway')
    f1.close()

print('this is outside the try-except-finally block')
