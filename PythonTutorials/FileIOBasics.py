# FIle IO Basics
"""
"r" - open a file for reading
"w" - open a file for writing
"x" - creates file if not exists
"a" - add more content to a file
"t" - text mode
"b" - binary mode
"+" - read and write to a file
"""


# f = open("text", "r")
# content = f.read()
# print(content)
# f.close()
#
# f = open("text2", "r")
# for line in f:
#     print(line)
# f.close()
#
# f = open("text2", "r")
# # print(f2.readline())
# print(f.readlines()) # returns a list of all the lines
# f.close()
#
# # writing and appending to a file
# f = open('text2','w')  # erase previous contents and write new
# f.write('\nthis is the next line i think line 4')
# f.close()
#
# f = open('text2','a') # append
# f.write('\nthis is the next line which is line 5')
# f.close()
#
# # read and write
# f = open('text2','r+')
# print(f.read())
# f.write('\nthis is line 6')
# f.close()
#
# f = open('text2')
# print(f.tell())
# print(f.readline())
# f.seek(20)
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()
#
# with open('text2') as q:
#     a = q.read(10)
#     print(a)
#
# q = open('text2')
# print(q.tell())
# print(q.readline())
# print(q.tell())
# print(q.readline())
# print(q.tell())
# print(q.readlines())
# q.close()

# with open('text2', 'r+') as r:
#     a = r.write("\nthis is line 8")
#     print(r.readlines())

def getdate():
    import datetime
    return datetime.datetime.now()

print(getdate())

#
#
# with open('Rohan_Food', 'w') as f:
#     f.write(str(getdate()))

# import os.path
# if os.path.exists('text2'):
#     mode = 'a'
# else:
#     mode = 'w'
# print(file_exists)