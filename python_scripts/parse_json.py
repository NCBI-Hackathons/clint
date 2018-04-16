import json
from pprint import pprint

#Opens the json file 
with open('data.json') as data_file:    
    data = json.load(data_file)

#print(len(data['parameters']))

#Creates an array for x, y and z locations as required
x = [];
for i in range(len(data['parameters'])):
    x.append(data['parameters'][i]['id'])
#print(x)
