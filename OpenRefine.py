import requests
import json 

url = 'http://127.0.0.1:3333/command/core/column-split'

# define the path to the file 
file_path = './Sheet1.csv'


#  parameters for creating the project from that file 
options = {
    'seperator': ',',
    'ignoreLines': 1 , 
    'projectName' : 'Test project 1'
}


# api request payload 
payload = { 
    'projectname' : options['projectName'],
    'ProjectTags' : '' , 
    'seperator': options['seperator'],
    'ignoreLines' : options['ignoreLines'],
    'storeBlankRows' : False , 
    'encoding' : 'UTF-8',
    'projectFileUpload' : (file_path, open(file_path,'rb'))
}

# http response of the api endpoint with the provided payload 

response = requests.post(url,files=payload)

#  project id (from response)

response_dict = json.loads(response.content)
project_id = response_dict['project']['id']




# Define the API endpoint URL for splitting the column
url = f'http://127.0.0.1:3333/command/core/column-split'

# Define the column name and separator to split on
column_name = 'full_name'
separator = ' '

# Define the options for splitting the column
options = {
    'mode': 'separator',
    'separator': separator,
    'regex': False,
    'removeOriginalColumn': True,
    'guessCellType': False
}

# Define the payload for the API request to split the column
payload = {
    'engine': {
        'facets': [],
        'mode': 'row-based'
    },
    'project': project_id,
    'columnName': column_name,
    'options': options,
    'onError': 'keep-original',
    'repeat': False,
    'repeatCount': 10
}

# Send an HTTP POST request to the API endpoint with the payload to split the column
response = requests.post(url, data=json.dumps(payload))

# Print the response
print(response.content)