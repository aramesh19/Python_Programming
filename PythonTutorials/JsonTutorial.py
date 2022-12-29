import json

data = '{"var1":"name1","var2":37}'

parsed = json.loads(data)
print(parsed)
print(parsed['var2'])
print(type(parsed))

data2 = {
    "channel_name" : "Elon"
    ,"cars" : ["Tesla","Porsche", "audi"]
    ,"plane" : ('Bombardier', 'LHM')
    ,"fridge" : ('roti', 99)
    ,'assets' : ['all','Few','land']
    ,"isbad" : False
}

jscomp = json.dumps(data2, sort_keys=True)
print(jscomp)
print(type(jscomp))