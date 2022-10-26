class Auto:
    def __init__(self, rek, Hnop, ATMnop):
        self.rek = rek
        self.Hnop = Hnop
        self.ATMnop = 0
    def kiihdytä(self, muutos):
        if muutos <=0:
                self.ATMnop-=muutos
        elif muutos >=0:
                self.ATMnop+=muutos

#pääohjelma
auto1=Auto("ABC-123",143, 0)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f"auton nopeus{auto1.ATMnop}")
auto1.kiihdytä(-200)
print(f"auton nopeus{auto1.ATMnop}")