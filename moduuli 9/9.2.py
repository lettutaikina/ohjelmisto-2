class Auto:
    def __init__(self, rek, Hnop):
        self.rek = rek
        self.Hnop = Hnop
        self.ATMnop = 0
    def kiihdytä(self, muutos):
        self.ATMnop+= muutos

        if self.ATMnop > self.Hnop:
            self.ATMnop = self.Hnop

        elif self.ATMnop < 0:
            self.ATMnop=0



#pääohjelma
auto1=Auto("ABC-123",142)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f"auton nopeus {auto1.ATMnop}km/h")
auto1.kiihdytä(-200)
print(f"auton nopeus {auto1.ATMnop}km/h")