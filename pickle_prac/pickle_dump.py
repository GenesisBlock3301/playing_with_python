import pickle

n = 5
data = []
for i in range(n):
    d = input(f"Enter [{i}]: ")
    data.append(d)

print(data)
file = open("important", "wb")

pickle.dump(data, file)
file.close()
print("done")
