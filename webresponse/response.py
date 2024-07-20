import requests

url = "https://atg.party/"  # Replace with your actual URL
response = requests.get(url)

if response.status_code == 200:
    print("200! 🍑")
else:
    print("exceeded 😕")
