import requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=cd55637ba0c6ca51bc1f2119930ebb24")
q = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=cd55637ba0c6ca51bc1f2119930ebb24")
print(r.text,'\n')
print(r.status_code)
#print(q.text)


# url = "www.w3schools.om"
# data = {
#     'P1':4,
#     'P2':6
# }
# r2 = requests.post(url = url, data = data)
