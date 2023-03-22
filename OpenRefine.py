import requests
import json 

url = 'http://localhost:3333/command/core'

payload = { 
           'project' : '1866105579170',
           'commands' : [
               {
                   'operations' : 'core/column-rename',
                   'oldColumnName': 'id',
                   'newColumnName': 'newId'
               }
           ]
}

response = requests.post(url , data = json.dumps(payload))

print(response.content) 