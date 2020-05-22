import requests
import json

# Initial API Info
covid19_th_api_address = 'https://covid19.th-stat.com/api/open/'
headers = {'Content-Type': 'text/JSON'}
address = covid19_th_api_address + 'today'

# Get Response
response = requests.get(address, headers=headers)

# If Error Show it
response.raise_for_status()

# Display JSON Format
results = response.json()
print(json.dumps(results))
print(results['Confirmed'])
