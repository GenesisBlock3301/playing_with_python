from jinja2 import Environment, FileSystemLoader

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

#load file of templates
file_loader = FileSystemLoader('templates')
#load file as a environmnet
env = Environment(loader=file_loader)
template = env.get_template('index.html')
output = template.render(persons=persons)
print(output)

