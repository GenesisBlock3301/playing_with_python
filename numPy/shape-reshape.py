import numpy as np

# oneDArray = np.array([1,2,3,4,5,6])
# print(oneDArray.shape)
# oneDArray.shape = (3,2)
# print(oneDArray)

arr = np.array([int(x) for x in input().split()])
arr.shape = (3,3)
print(arr)