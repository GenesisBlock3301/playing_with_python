import numpy
n , m = list(map(int,input().split()))
arr1 = [int(x) for x in input().split()][:n]
arr2 = [int(x) for x in input().split()][:m]

arr = numpy.array([arr1,arr2])
print(numpy.transpose(arr))
print(arr.flatten())