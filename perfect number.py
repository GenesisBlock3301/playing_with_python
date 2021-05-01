sum1 = 0
for i in range(1,100):
    for j in range(1,i):
        if i%j == 0:
            sum1 += j
    if sum1 == i and i != 1:
        print(i)
    sum1=0
        

            
