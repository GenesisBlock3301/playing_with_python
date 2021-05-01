import json

with open('datafile.json') as read_file:
    #load takes a file as a parameter
    #load means read some file
    data = json.load(read_file)

#make string
data = json.dumps(data)
print(data)

#loads takes a string as a parameter
data_string = json.loads(data)
print(type(data_string))
