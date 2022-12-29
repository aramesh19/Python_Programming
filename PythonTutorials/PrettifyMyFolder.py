import os

# def removeFiles(filen):
#     DNotDis = open(filen)
#     l = (DNotDis.read())
#     var = (l.split('\n'))
#     DNotDis.close()
#     return var
#
# def army(pathn, filen, ext):
#     filen=filen
#     pathn=pathn
#     os.chdir(pathn)
#     count = 0
#     var = removeFiles(filen)
#     for f in os.listdir():
#          f_name, f_ext = os.path.splitext(f)
#          if f_ext == f'.{ext}':
#              newName = f'{str(count)}{f_ext}'
#              count += 1
#              os.rename(f,newName)
#              pass
#          if f_name not in var:
#              tn = f_name.title()
#              new_name = f'{tn}{f_ext}'
#          else:
#              new_name = f'{f_name}{f_ext}'
#          os.rename(f,new_name)
#
# if __name__ == '__main__':
#     pathn= r'D:\MIsc' #input('Enter Path Name:')
#     filen= r"D:\MIsc\ext12.txt" #input('Enter File Name Which Contain Name Of Files Not TO Alter: ')
#     ext=".jpg"
#     army(pathn,filen,ext)


def soldier(path, file, format):
    os.chdir(path)
    i=1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
    #print(filelist)

    for z in files:
        if z not in filelist:
            os.rename(z, z.capitalize())

        if os.path.splitext(z)[1] == format:
            os.rename(z, f"{i}{format}")
            i+=1

soldier(r"D:\MIsc",r"D:\MIsc\ext12.txt",".jpg")


