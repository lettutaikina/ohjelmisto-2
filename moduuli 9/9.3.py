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



#pääohjelma
auto1=Auto("ABC-123",142)
auto1.kiihdytä(60)
print(f"auton nopeus {auto1.ATMnop} km/h")
#tuntimäärämetodi
auto1.kulje(1.5)