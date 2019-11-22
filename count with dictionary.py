st="aeiou"
dic = {}
for i in st:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1
print(dic)
