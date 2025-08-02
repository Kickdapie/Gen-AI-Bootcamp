import requests

r = requests.get("http://localhost:8000/hi/Sashank")
print(r.json())