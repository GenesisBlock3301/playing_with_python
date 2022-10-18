import sys

flag = sys.argv[1]
value = float(sys.argv[2])

if flag == "-c":
    celsius = (value - 32)/1.8
    print(celsius)
else:
    fahrenheit = value*1.8+32
    print(fahrenheit)