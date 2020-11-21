from jinja2 import Template

name = 'Sifat'
age = 24

tm = Template("My name is {{name}} and age is {{age}}")
msg = tm.render(name=name,age=age)
print(msg)
