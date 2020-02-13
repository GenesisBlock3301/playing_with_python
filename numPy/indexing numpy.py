import numpy as np

arr = np.array([
    [-1,2,0,4],
    [4,-0.5,6,0],
    [2.6,0,7,8],
    [3,-7,4,2.0]
])

print(arr)

print("Slice array: ")
slice_arr = arr[:2,::-1]
print(slice_arr)