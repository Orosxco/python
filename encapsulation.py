class computer:
    def __init__(self):
        self.__maxprice = 9000
    
    def sell(self):
        print(f"Selling price: {self.__maxprice}")

    def setprice(self, price):
        self.__maxprice = price
    
c = computer()
c.sell()

c.__maxprice = 10000
c.sell()

c.setprice(8500000)
c.sell()