from jinja2 import Template

person = {'name':'Sifat','age':24}

tm = Template("My name is {{person['name']}} and age is {{person['age']}}")
msg = tm.render(person=person)
print(msg)