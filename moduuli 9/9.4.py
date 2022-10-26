import random
from tabulate import tabulate
class Auto:
    def __init__(self, rek, Hnop):
        self.rek = rek
        self.Hnop = Hnop
        self.ATMnop = 0
        self.Kmatka=0
    def kiihdytä(self, muutos):
        self.ATMnop+= muutos

        if self.ATMnop > self.Hnop:
            self.ATMnop = self.Hnop

        elif self.ATMnop < 0:
            self.ATMnop=0

    def kulje(self,tunnit):
        self.Kmatka+=tunnit*self.ATMnop
        print(f"kuljettu matka on {self.Kmatka}km")



#pääohjelma looppi
autot=[]
pisin=0

for i in range(10):
    auto1=Auto(f"ABC-{i+1}",random.randint(100,200))
    autot.append(auto1)

#kilpailu
if pisin < 10000:
    for auto in autot:
        auto.kiihdytä(random.randint(-10,15))

    for auto in autot:
        auto.kulje(1)
    if auto.Kmatka > pisin:
        auto.Kmatka=pisin

Tuloslista=[]

for auto in autot:
    lista=[auto.rek, auto.Hnop, auto.ATMnop, auto.Kmatka]
    Tuloslista.append(lista)



print(tabulate(Tuloslista, headers=['Rekisteri', 'Huippunopeus', 'Nopeus','Kuljettu matka'],tablefmt='rounded_outline'))
