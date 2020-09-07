import re

text = 'My mail are nur-15-1463@diu.edu.bd , mdnuraminsifat380@gmail.com and example@yahoo.com'
# \W means non-digit ,\w means digit
pattern = '\w+[\W|\d]*@[\w]+[\W]*[\w]+[\W]*[\w]+'
# match = re.search(pattern,text)
match = re.findall(pattern,text)
print(match)