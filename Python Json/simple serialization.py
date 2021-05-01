import json

data = {
    'president': {
        "name": "Nur Amin Sifat",
        "species": "Betelgeusian"
    }
}

# with open("datafile.json","w") as write_file:
#     json.dump(data,write_file)
    # print(type(json.dump(data,write_file)))

json_string = json.dumps(data,indent=4)
print(json_string)