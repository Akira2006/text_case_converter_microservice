import requests

url = "http://localhost:5002/convert"

data = {
    "text": "hello world",
    "case": "upper"
}

response = requests.post(url, json=data)

print("Response:")
print(response.json())