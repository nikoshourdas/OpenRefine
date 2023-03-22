import requests
import json

# Define the OpenRefine project URL and API key
refine_url = "http://localhost:3333/"
api_key = "your_api_key"

# Define the CSV file to clean and the project name


# Get the project ID
project_id = 1866105579170

# Remove duplicate rows
response = requests.post(refine_url + "/command/core/multistep",
                         params={"project": project_id, "operations": json.dumps([{"op": "remove-duplicates"}])},
                         headers={"X-OpenRefine-Api-Key": api_key})

# Export the cleaned data as CSV
response = requests.post(refine_url + "/command/core/export",
                         params={"project": project_id, "format": "csv", "engine": "python"},
                         headers={"X-OpenRefine-Api-Key": api_key})

# Write the exported data to a file
with open("cleaned_data.csv", "wb") as f:
    f.write(response.content)
