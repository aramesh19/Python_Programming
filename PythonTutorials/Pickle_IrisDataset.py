import requests
import pickle

#data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#data = "C:\Users\ramesh.annasamudram\Documents\Python_Programming\PythonTutorials\iris.data"
with open('iris.data') as q:
    data = q.readlines()
#print(data)

l1 = []
for sub in data:
    l1.append(sub.replace("\n",""))
#print(l1)
l2 = [item.split(',') for item in l1 if len(item)!=0]
print(l2)

with open('irispickle.pkl','wb') as f:
    pickle.dump(l2, f)

## to read the pickle file
with open('irispickle.pkl','rb') as q:
    print(pickle.load(q))
