# import math


def toCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def toFahrenhiet(celsius):
    return (celsius * 9 / 5) + 32


def tryToConvert(temperature, convert):
    if not temperature:
        return ''
    val = convert(temperature)
    return val


def scaleName():
    dic = {
        'c': "Celsius",
        'f': 'Fahrenheit'
    }
    return dic


class TemperatureInput:

    def __init__(self,scale ,temparature):
        self.scale = scale
        self.temperature = temparature

    def show(self):
        unit = scaleName()
        return f"Temperature is {self.temperature:0.2f} {unit[self.scale]}"


class Calulator:

    def calculate(self):
        print("Enter your scale name: ")
        scale = input()
        temperature = input("Enter your temperature: ")
        if scale == 'c':
            celsius = tryToConvert(float(temperature), toFahrenhiet)
            t = TemperatureInput(scale,celsius)
            print(t.show())

        elif scale == 'f':
            fahrenheit = tryToConvert(float(temperature), toCelsius)
            t = TemperatureInput(scale, fahrenheit)
            print(t.show())


if __name__ == "__main__":
    calc = Calulator()
    calc.calculate()