from multiprocessing import *

# number of CPU core
# print(cpu_count())

def myFunc():
    print("Hello world")

def lang_func(lang):
    print(lang)

if __name__ == '__main__':
    # proc = Process(target=myFunc)
    # proc.start()
    # proc.join()
    langs = ['C','Python','JAVA','PHP']
    process = []
    for i in langs:
        proc = Process(target=lang_func,args=(i,))
        process.append(proc)
        proc.start()
    # for p in process:
    #     p.join()