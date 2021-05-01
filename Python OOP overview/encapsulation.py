class Computer:

    def __init__(self):
        self.__maxprize = 900

    def sell(self):
        print(f"Selling is 800 and maximum prize is {self.__maxprize}")

    def setMaxPrize(self,price):
        self.__maxprize = price
        return f"The updated price is {self.__maxprize}"


c = Computer()
c.sell()
c.__maxprize = 1000
c.sell()
c.setMaxPrize(10000)
c.sell()