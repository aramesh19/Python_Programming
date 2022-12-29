import pickle

# pickling a python object.
cars = ['Audi','Porsche']
t = ('this','that')

file = 'details.pkl'

fileobj = open(file, 'wb')
pickle.dump(t, fileobj)
fileobj.close()

file = 'details.pkl'
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)

print(mycar)