import re

text = "My phone number is 017-588-07212 and 019-491-168736"
# pattern = r'\d\d\d-\d\d\d\-\d\d\d\d\d'
# for indexing we use ()
pattern = r'(\d{3})-(\d{3})-(\d{5})'
phone_number = re.search(pattern,text)
# print("Phone number is: ",phone_number.group(3))

#pipe searching
match = re.search(r"man|woman","This man is best friend")
print(match.group())

# and
match = re.search(r".man","This man a& woman is best friend")
print(match.group())
