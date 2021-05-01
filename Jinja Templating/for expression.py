from jinja2 import Template

t = Template("My favorite number: {% for i in range(1,11)%}{{i}} {% endfor %}")
msg = t.render()
print(msg)

