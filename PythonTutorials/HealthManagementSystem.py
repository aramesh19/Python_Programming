import os
from os.path import exists

RW = input("Do you want to read data or write data: \n Type R for read, W for write: ")
C = input('Who do you want to log data for?\n Type R for Rohan, H for Harry, C for Chandra: ')
FE = input('Do you want to log/See data for Food or Exercise?\n Type F for Food, E for Exercise: ')


def getdate():
    import datetime
    return datetime.datetime.now()


def write_f(filename, wa_mode, message):
    with open(filename, wa_mode) as f:
        f.write('\n[' + str(getdate()) + ']')
        f.write(message)


if RW == 'W':
    if C == 'R':
        if FE == 'F':
            Food = input('Enter details of the food eaten: ')
            if os.path.exists('Rohan_Food'):
                mode = 'a'
            else:
                mode = 'w'
            write_f('Rohan_Food', mode, Food)
        if FE == 'E':
            Exe = input('Enter details of exercise: ')
            if os.path.exists('Rohan_Exercise'):
                mode = 'a'
            else:
                mode = 'w'
            write_f('Rohan_Exercise', mode, Exe)
    if C == 'H':
        if FE == 'F':
            Food = input('Enter details of the food eaten: ')
            if os.path.exists('Harry_Food'):
                mode = 'a'
            else:
                mode = 'w'
            write_f('Harry_Food', mode, Food)
        if FE == 'E':
            Exe = input('Enter details of exercise: ')
            if os.path.exists('Harry_Exercise'):
                mode = 'a'
            else:
                mode = 'w'
            write_f('Harry_Exercise', mode, Exe)
    if C == 'C':
        if FE == 'F':
            Food = input('Enter details of the food eaten: ')
            if os.path.exists('Chandra_Food'):
                mode = 'a'
            else:
                mode = 'w'
            write_f('Chandra_Food', mode, Food)
        if FE == 'E':
            Exe = input('Enter details of exercise: ')
            if os.path.exists('Chandra_Exercise'):
                mode = 'a'
            else:
                mode = 'w'
            write_f('Chandra_Exercise', mode, Exe)
if RW == 'R':
    if C == 'R':
        if FE == 'F':
            with open('Rohan_Food', 'r+') as f:
                [print(line) for line in f.readlines()]
        if FE == 'E':
            with open('Rohan_Exercise', 'r+') as f:
                [print(line) for line in f.readlines()]
    if C == 'H':
        if FE == 'F':
            with open('Harry_Food', 'r+') as f:
                [print(line) for line in f.readlines()]
        if FE == 'E':
            with open('Harry_Exercise', 'r+') as f:
                [print(line) for line in f.readlines()]
    if C == 'C':
        if FE == 'F':
            with open('Chandra_Food', 'r+') as f:
                [print(line) for line in f.readlines()]
        if FE == 'E':
            with open('Chandra_Exercise', 'r+') as f:
                [print(line) for line in f.readlines()]
