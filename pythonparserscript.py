import os
import json
import requests

def create_files(data):
    # Create a sub-directory if it doesn't exist
    if not os.path.exists('files'):
        os.makedirs('files')

    # Iterate over each item in the JSON data.
    # we assume that the JSON data has a key named 'samples'
    # which contains an array of objects, each containing 'id' and 'name' fields.
    # it itereates over each item in the 'samples' array. extracting the id and name fields
    # and creates a file named <id>.txt in the files/ sub-directory with the 'name' field as the content.
    for item in data['samples']:
        # Extract id and name
        item_id = item.get('id')
        item_name = item.get('name')

        # Create a file named <id>.txt in the files/ sub-directory
        with open(f'files/{item_id}.txt', 'w') as file:
            file.write(item_name)

# URL to fetch JSON data
url = 'http://localhost:5000/data'  # Replace with your actual URL

# Fetch JSON data
response = requests.get(url)
if response.status_code == 200:
    # Parse JSON data
    json_data = response.json()

    # Create files
    create_files(json_data)
else:
    print("Failed to fetch JSON data:", response.status_code)
