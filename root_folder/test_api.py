import requests

url = 'http://localhost:5000/predict'

# Valid request
data = {'location': 'Gasabo', 'sqft': 1500, 'rooms': 3}
response = requests.post(url, json=data)
print('Valid request response:', response.json())

# Invalid location
data_invalid = {'location': 'InvalidLocation', 'sqft': 1500, 'rooms': 3}
response = requests.post(url, json=data_invalid)
print('Invalid location response:', response.json())

# Missing field
data_missing = {'location': 'Gasabo', 'sqft': 1500}
response = requests.post(url, json=data_missing)
print('Missing field response:', response.json())

# Invalid sqft
data_invalid_sqft = {'location': 'Gasabo', 'sqft': -100, 'rooms': 3}
response = requests.post(url, json=data_invalid_sqft)
print('Invalid sqft response:', response.json())