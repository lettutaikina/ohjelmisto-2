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


class kilpailu:
    def __init__(self, nimi, km, autot):
        self.nimi=nimi
        self.km=km
        self.Tuloslista = []
        self.autot=autot

    def tunti_kuluu(self):
        for I in range(len(self.autot)):
            self.autot[I].kiihdytä(random.randint(-10, 15))
            self.autot[I].kulje(1)



    def tulosta_tilanne(self):

        for auto in autot:
            lista = [auto.rek, auto.Hnop, auto.ATMnop, auto.Kmatka]
            self.Tuloslista.append(lista)
        print(tabulate(self.Tuloslista, headers=['Rekisteri', 'Huippunopeus', 'Nopeus', 'Kuljettu matka'],tablefmt='rounded_outline'))

    def kilpailu_ohi(self):
        for I in range(len(self.autot)):
            if self.autot[I].Kmatka>=self.km:
                return True
        return False




#pääohjelma
#8000km välein "Suuri romuralli"


autot = []
for i in range(10):
    auto1 = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot.append(auto1)

kilpailu1 = kilpailu("Suuri romuralli", 8000, autot)

while kilpailu1.kilpailu_ohi()==False:
    kilpailu1.tunti_kuluu()
    if kilpailu1.kilpailu_ohi()==True:
        kilpailu1.kilpailu_ohi()
        kilpailu1.tulosta_tilanne()
        print("kilpailu ohi")




