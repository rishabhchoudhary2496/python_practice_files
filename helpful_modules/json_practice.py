# import json
# #seriliazing object to json
# person = {'name':'Dexter','age':30,'gender':"Male"}
# json_object = json.dumps(person)
# print(json_object)
# print(json.load(json_object))

import requests
import pprint
import json

# r = requests.get('https://jsonplaceholder.typicode.com/users')
# status = r.status_code
# headers = r.headers
# history = r.history
# print(status)
# print(headers)
# print(history)

# data = {   
#     "name": "brahmi",
#     "username": "Bret",
#     "email": "Sincere@april.biz",
#     "address": {
#       "street": "Kulas Light",
#       "suite": "Apt. 556",
#       "city": "Gwenborough",
#       "zipcode": "92998-3874",
#       "geo": {
#         "lat": "-37.3159",
#         "lng": "81.1496"
#       }
#     },
#     "phone": "1-770-736-8031 x56442",
#     "website": "hildegard.org",
#     "company": {
#       "name": "Romaguera-Crona",
#       "catchPhrase": "Multi-layered client-server neural-net",
#       "bs": "harness real-time e-markets"
#     }}

# pr = requests.post('https://jsonplaceholder.typicode.com/users',data=data)

string = '{"var1":"jerry","var2":58}'
#parsing json to dictionary
parse = json.loads(string)
print(parse)
data = {
    "channel":"hbo",
    "show":"GOT",
    "characters":('tyrion','john','arya','danerys','sansa'),
} 

print(json.dumps(data,sort_keys=True))
#dump (dict,filepath where dictionary is)
#load alos takes file path insted of string