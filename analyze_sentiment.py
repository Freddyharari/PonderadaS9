import requests
import json

url = "https://language.googleapis.com/v1/documents:analyzeSentiment?key=SUA_CHAVE_DE_API"
headers = {
    "Content-Type": "application/json",
}

payload = {
    "document": {
        "type": "PLAIN_TEXT",
        "content": "I am very happy with the service!"
    },
    "encodingType": "UTF8"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
