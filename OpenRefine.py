import json 
import requests 

project_url = 'http://localhost:3333'

project_id = 1866105579170


# make a facet request that sorts by id number 
facet = {
    "op": "core/column-facet",
    "column": "id_number",
    "expression": "value.toNumber()",
    "facet": {
        "type": "list",
        "name": "id_number_facet",
        "choiceCount": 50
    }
}
# Send the request to OpenRefine
response = requests.post(
    f"{project_url}",
    data={
        'project': project_id,
        'operations': json.dumps([facet])
    }
)

if response.status_code == 200: 
    print("facet request successful")

else : 
    print(f"Facet request failed with status code {response.status_code}")
    
    
# response_data = response.json()
# # print(response_data)

# # print(response)


