import re

text = 'My phone is 111-222-3333 , call me later.'
pattern = 'phone'
#search() retunrn first find value
match = re.search(pattern,text)
print(match)
print(match.span())
print(match.start(),match.end())

text2 = 'My phone is 111-222-3333 , call me later phone'
match = re.search(pattern,text2)
print(match)

#find all same value from text2
all_match = re.findall(pattern,text2)
print(all_match)

for i in re.findall(pattern,text2):
    print(i)

print("Phone nubber")
text = "My phone number is 017-588-07212 and 019-491-168736"
# pattern = r'\d\d\d-\d\d\d\-\d\d\d\d\d'
pattern = r'\d{3}-\d{3}-\d{5}'
phone_number = re.search(pattern,text)
print("Phone number is: ",phone_number.group())
phone_number_findall = re.findall(pattern,text)
print(f"Fins all phone number: {phone_number_findall}")
