import os
print(dir(os))
print(os.getcwd())
#os.chdir('C://')
print(os.getcwd()) # Current working directory is very important.
# the program will first look for files in the Current working directory.
# Listdir
#os.chdir("C:\Users\ramesh.annasamudram\Documents\Python_Programming\PythonTutorials")
#print(os.getcwd())
print(os.listdir('C://')) # lists all the files/folders in that folder
#os.mkdir("ThisNew") # create a new folder
#os.makedirs("Where/When") # create a folder + subfolder
#os.rename("filename","filenamedd") # rename a file
#os.rename("filenamedd","filename")
# environment variables
print(os.environ.get('Path'))

print(os.path.join('C://', 'filename'))
print(os.path.join('C:/', '/filename'))

print(os.path.exists('C:/Ramesh'))
print(os.path.exists('C://Program Files'))
print(os.path.isfile('C://Program Files')) # checks for file name
print(os.path.isdir('C://Program Files')) # checks for folder name
