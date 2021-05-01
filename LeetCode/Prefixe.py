strs = ["flower", "low", "flight"]
check = list(strs[0])
m = 1
c = 1
for t in range(len(check)):
    if m < len(strs):
        if any(map(lambda x: strs[m].startswith(x),check)):
            print("ok")
        else:
            break
        check = check[c:]
    c += 1
    m += 1
