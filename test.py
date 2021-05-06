import json
import requests
res = requests.get("http://api.open-notify.org/astros.json")
data = json.loads(res)
user_name = data['people']
result[]
for i in user_name:
  result.append(i['name'])
result.sort()
for i in result:
  print(i)