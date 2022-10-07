import pickle

file = open("important", "rb")
data = pickle.load(file)

file.close()
cnt = 0
for item in data:
    print(f"The data {cnt} is {item}")
    cnt+=1


