

import requests


headers = {'Authorization': 'Bearer e7de52e106e81f971085f8210c5f1ad09bfb0d96'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
