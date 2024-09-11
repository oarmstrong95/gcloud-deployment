import requests

# The URL of the API endpoint
url = 'https://gclouddeployment-329329814844.europe-west2.run.app'

# The data to be sent in the request body
data = {'name': 'Oliver Armstrong'}

# The headers for the request
headers = {'Content-Type': 'application/json'}

# Send a POST request to the API
response = requests.post(url, json=data, headers=headers)

# Print the response from the API
print(response.text)
