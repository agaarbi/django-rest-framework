import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.get(endpoint, json ={"query":"Hello world!"}) # API -> Method
print(get_response.text)
print(get_response.status_code)