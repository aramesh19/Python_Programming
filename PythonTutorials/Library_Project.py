# Create a library class
# display book
# lend book
# add book
# return Book

class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'the following books are available in : {self.name}')
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been updated. The book is available now")
        else:
            print(f'Book is already being used by {self.lendDict[book]}')

    def addBook(self, book):
        self.bookslist.append(book)
        print("book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    RamsLib = Library(['Python','Sub Conscious Mind','C++','MF basics'],'Best Library')

    while(True):
        print(f'Welcome to the {RamsLib.name} . Enter a choice to continue')
        print('1. Display books')
        print('2. lend a book')
        print('3. Add a book')
        print('4. Return a book')
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print('Enter a valid choice')
            continue
        else:
            user_choice = int(user_choice)
        if user_choice ==1:
            RamsLib.displayBooks()
        elif user_choice == 2:
            book = input('Enter the name of the book you want to lend:')
            user = input('Enter your name: ')
            RamsLib.lendBook(user, book)
        elif user_choice == 3:
            book = input('Enter the name of the book you want to add: ')
            RamsLib.addBook(book)
        elif user_choice == 4:
            book = input('Enter the name of the book you want to return: ')
            RamsLib.returnBook(book)
        else:
            print('Not a valid option')

        print('Press q to quit and c to continue')
        user_choice2 = ""
        while(user_choice2!='c' and user_choice2 !='q'):
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            if user_choice2 == 'c':
                continue