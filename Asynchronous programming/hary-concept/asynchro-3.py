import os
from threading import Thread
import time


threads = [
    Thread(target=lambda: time.sleep(3)) for i in range(1000)
]
[t.start() for t in threads]
print(f"PID = {os.getpid()}")
[t.join() for t in threads]