import json

data = '{"var1":"Nur","var2":56}'

parsed = json.loads(data)
print(parsed)