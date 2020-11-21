from jinja2 import Template

name = input("Enter your name")
tem = Template("Hello {{name}}")
msg = tem.render(name=name)
print(msg)
