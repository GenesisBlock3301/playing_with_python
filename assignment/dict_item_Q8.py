import sys

key, value = sys.argv[1:3]
dic = {
    "Hydrogen": 1, "Helium": 4
}
if key in dic:
    print("Element already present")
if key in dic and dic[key] != int(value):
    print("Element present, but the value is different")
else:
    dic[key] = int(value)
    print("Element added and updated dictionary", dic)


