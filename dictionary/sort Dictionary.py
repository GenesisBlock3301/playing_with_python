x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

m = sorted(x.items(),key=lambda x: x[1])
print(m)

#reverse
n = 112
res = 0
while n > 0:
    tem = n%10
    res = res*10+tem
    n = n//10
print(res)

#item suming value
n = 112
res = 0
while n > 0:
    tem = n%10
    res+=tem
    n = n//10
print(res)

#