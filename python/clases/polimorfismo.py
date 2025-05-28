#lissett fuentes
#20-05-2025

class Cafe():
    def que_soy(self):
        print("soy un café")

class Te():
    def que_soy(self):
        print("soy un té")

def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Te())
