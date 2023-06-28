import requests
import json

url = 'http://127.0.0.1:8000/incoming_data'
data = {
    'Post_Name': 'the India',
    'Post_Content': 'Place of Cultures',
}
#"CL-X-TOKEN": "t2MG02BRE4xgIEQ0",
json_data = json.dumps(data)
headers = {
    "CL-X-TOKEN": "FvO1mB3TgaCFttj6",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, json=json_data, headers=headers)
print(url, data, headers, response)

if response.status_code == 200:
    print('Data successfully processed')
else:
    print(response.text)

    #print(response.content)  # Print the JSON response content in the console
