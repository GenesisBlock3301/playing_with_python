import time
def searcher():
    #Some 4 second time consuming cost
    b = "My name is Nur Amin Sifat"
    # print(b)
    time.sleep(4)

    while True:
        text = (yield)
        if text in b:
            print("Your text in the books")
        else:
            print("Text is not in the book")


search = searcher()
print("Search start")
next(search)
print("Next method run")
search.send("Sifat")
input("Press any key: ")
search.send("Nur Amin")
search.close()
search.send("Nur Amin")

