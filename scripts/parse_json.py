####################################################
##This file is used to parse the JSON file and extract the 
#data and save in lists. 
#The lists can be used as params to be passed to the http://neurosynth.org/api/v2/ API

# NCBI Hackathon Team: brainimages


####################################################
import json
import requests
from pprint import pprint

#Opens the json file 
with open('data.json') as data_file:    
    data = json.load(data_file)

#print(len(data['parameters']))

#Creates an array for x, y and z locations as required
x = [];
for i in range(len(data['parameters'])):
    x.append(data['parameters'][i]['id'])
print(x)

####################################################
# This function used to query the Neurosynth API, with input parameters as lists that contain the keys and values
#input: url; querytype for e.g. 'locations', 'images', 'gene' etc; query:values obtained from
#parsed files above

#output: output from the query to Neurosynth

####################################################

#Function definition for querying Neurosynth
def get_neurosynth(url, querytype, query):
    if querytype == 'locations':
        result = requests.get(url+querytype+'/', params=query)
        #return result.url #Checks the url
        return result.content
    elif querytype == 'symptom':
        result = requests.get(url+querytype+'/', params=query)
        return result.content

voxel_list = {'x':'2', 'y':'4', 'z':'5'}
url ='http://neurosynth.org/api/v2/'

################################

#Test data set (1 location) with function call to get_neurosynth

data_new = get_neurosynth(url, 'locations', voxel_list)
print(data_new)

################################