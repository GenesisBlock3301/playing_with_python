# Read all line
with open('text.txt','r') as f:
    data = f.read()
    print(data)
r = open('text.txt','r').read()
print(r)

# read one line
ReadOneLine = open('text.txt','r').readline()
print("Read One line: ",ReadOneLine)
with open('text.txt','r') as f:
    data = f.readlines()
    print(data)