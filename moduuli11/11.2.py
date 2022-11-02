from tabulate import tabulate

class Auto:
    def __init__(self, rek, Hnop, ATMnop):
        self.rek = rek
        self.Hnop = Hnop
        self.ATMnop =ATMnop
        self.Kmatka=0

    def tulosta_tiedot(self):
        print(self.rek)

    def kulje(self,tunnit):
        self.Kmatka+=tunnit*self.ATMnop
        print(f"kuljettu matka on {self.Kmatka}km")
        
class Sähköauto(Auto):
    def __init__(self,rek,Hnop,ATMnop, akkukapa):
        super(Sähköauto, self).__init__(rek,Hnop,ATMnop)
        self.akkukapa=akkukapa

    def tulosta_tiedot(self):
        super(Sähköauto, self).tulosta_tiedot()
        print(f"Huippunopeus {self.Hnop}km/h\nAkkukapasiteetti {self.akkukapa}kWh")
        
    
class Polttomoottoriauto(Auto):
    def __init__(self,rek,Hnop,ATMnop,bensakok):
        super(Polttomoottoriauto, self).__init__(rek,Hnop,ATMnop)
        self.bensakok=bensakok

    def tulosta_tiedot(self):
        super(Polttomoottoriauto, self).tulosta_tiedot()
        print(f"Huippunopeus {self.Hnop}km/h\nTankinkoko {self.bensakok} litraa")

#PÄÄOHJELMA
autot=[]
#rek, maxnop, atmnop, koko
autot.append(Sähköauto("ABC-15",180,20,52.5))
autot.append(Polttomoottoriauto("ABC-123",165,45,32.3))
for A in autot:
    A.kulje(3)
for I in autot:
    I.tulosta_tiedot()

