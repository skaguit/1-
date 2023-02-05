class Phone():
    def __init__(self, number, model, weight):
        self.number = number
        self.midel = model
        self.weight = weight

    #def __init__(self, number, model):
        #self.number = number
        #self.midel = model

    #def __init__(self):
        #pass

    def receiveCall(self, name):
        print(f'Звонит {name}')

    def getNumber(self):
        return self.number

    def sendMessage(self, *args):
        self.numbers = args
        for i in self.numbers:
            print(i)


phone1 = Phone('+79001112233', 'm1', 15)
phone2 = Phone('+79004445566', 'm2', 20)
phone1.receiveCall('Виталий')
print(phone2.getNumber())
phone1.sendMessage('+79004445566', '+79017778899')