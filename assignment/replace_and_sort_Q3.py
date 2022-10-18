import sys

replace_value = sys.argv[1]
arr = ['Here', "Some", "Any", "There"]
arr[-1] = replace_value
arr.sort()
print(arr)
