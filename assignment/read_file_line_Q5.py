import sys

file_name = sys.argv[1]
arr = list()
with open(file_name, "r") as f:
    for i in f.readlines():
        if i[-1] == "\n":
            arr.append(i[:-1].split(","))
        else:
            arr.append(i.split(","))

for i in arr:
    print(i)