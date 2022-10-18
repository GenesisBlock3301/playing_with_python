import sys


def show_bars_func(dash_number):
    for i in dash_number:
        print("-"*int(i))


dash_number = sys.argv[1:]
show_bars_func(dash_number)