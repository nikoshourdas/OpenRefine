import requests
import json 
import requests
import json

# API endpoint URL for creating a project from a file upload
# GBIF DATASET
api_url = 'http://192.168.15.110:3333/project?project=1866105579170'

# File path and name of the CSV file to upload

# Send a GET request to the OpenRefine API to obtain a CSRF token
csrf_response = requests.get(api_url)
csrf_token = csrf_response.cookies['csrf_token']

# Configure the project creation request payload
payload = {
    'projectName': 'my-new-project',
    'files': [
        {
            'fileName': 'my-data.csv',
            'upload': 'file://' + csv_file_path,
            'options': {
                'encoding': 'UTF-8',
                'separator': ','
            }
        }
    ]
}

# Convert the payload to JSON format
payload_json = json.dumps(payload)

# Send the project creation request to OpenRefine API
response = requests.post(api_url, data=payload_json)

# Print the response from the API
print(response.text)
