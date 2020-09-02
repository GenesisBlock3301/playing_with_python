import threading
# import time

# start = time.time()
class Call(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

obj = Call(name='Sending message hello')
obj1 = Call(name='Rec. msg byee.')
obj.start()
obj1.start()
# end = time.time()
# print("Time cost",end-start)