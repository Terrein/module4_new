import http.client
import json
from pprint import pprint



RANDOM_DATA = True
conn = http.client.HTTPSConnection("pumpskill.ru")
conn.request("GET", f"/cases/api/python-basic/users-and-friends/{'?r=0' if not RANDOM_DATA else ''}")
response = conn.getresponse()
data = json.loads(response.read().decode("utf-8"))

users = data["users"]
countries = data["countries"]

# conn = requests.get(f"https://pumpskill.ru/cases/api/python-basic/users-and-friends/{'?r=0' if not RANDOM_DATA else ''}")

# print(conn.json())
