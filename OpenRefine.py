import requests
import json 

url = 'http://localhost:3333' 
# /command/core
# we use this end point to automate the data manupulation tasks we want to process 

# project_ID = '2318446209232'
# column_name = 'product-id'

# payload = { 
#            'project' : '2318446209232',
#            'commands' : [
#                {
#                    'operations' : 'core/column-rename',
#                    'oldColumnName': 'product-id',
#                    'newColumnName': 'newId'
#                }
#            ]
# }

csrf_token = requests.get(url + '/csrf_token')
print(csrf_token.text)

# payload = {
#     'projectID': project_ID,
#     'columnName': column_name,
#     'expression': f'value.replace("product-id", "new_label")'
# }
# headers = {'Content-Type': 'application/json'}

# response = requests.post(url, data=json.dumps(payload), headers=headers)


# print(response.status_code)
# Parse the JSON response
# response_json = json.loads(response.content)

# Print the response status
# print(response_json['code'])