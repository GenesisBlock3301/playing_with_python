from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

obj = Hello()
obj2 = Hi()
# run the program, its start() automatically run
obj.start()
obj2.start()
# all threading complete before main function call that means Bye print at the last .
obj.join()
obj2.join()
print("Bye")