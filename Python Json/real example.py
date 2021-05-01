import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(type(response.text))
todos = json.loads(response.text)
# print(type(todos))
print(todos)