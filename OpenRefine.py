import requests
import json 

url = 'http://localhost:3333/command/core' 
# /command/core
# we use this end point to automate the data manupulation tasks we want to process 


payload = { 
           'project' : '2318446209232',
           'commands' : [
               {
                   'operations' : 'core/column-rename',
                   'oldColumnName': 'product-id',
                   'newColumnName': 'newId'
               }
           ]
}

response = requests.post(url , data = json.dumps(payload))

print(response.content) 