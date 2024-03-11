import requests
import json

# Assuming 'url', 'link', and 'jwt_token' are defined somewhere in your code
url = "http://127.0.0.1:8000/setlink"
link = "https://drive.google.com/drive/folders/1mY4IfFl56tK3eE5tEExfGaRqc8fTh-0l"
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTAxNjA4NzEsInN1YiI6IjEifQ.e7feUdBio8_Y5RCKgGI_gBrgYDHLqbbYU6viMiXO1Mc"

# JSON data including the link
data = {
    "link": link
}

# Set up the request headers with the JWT token
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"  # Assuming JSON data is being sent
}

# Make the POST request with the data and headers 
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.json())
# Check the response
# if response.status_code == 202:
#     print("Request successful!")
#     print(response.json())  # Print the response data
# else:
#     print("Request failed:", response.text)  # Print error message if request fails
