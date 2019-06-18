n=int(input())
number=[]
inn=0
out=0
for i in range(1,n+1):
    number.append(input())
for k in number:
    if (int(k)>= 10) and (int(k)<= 20):
        inn+=1
    else:
        out+=1
print ("%d in"%inn)
print ("%d out"%out)
