import sys

# here reference count one
var1 = [1]
# reference count 2
var2 = var1
# reference count 3
var3 = var2
# now print 3+extra 1
print(sys.getrefcount(var3))

