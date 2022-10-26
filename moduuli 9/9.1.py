class Auto:
    def __init__(self, rek, Hnop, ATMnop, Kmatka):
        self.rek = rek
        self.Hnop = Hnop
        self.ATMnop = 0
        self.Kmatka = 0
        print(f"auton rekisterinumero on {self.rek}\nhuippunopeus on {self.Hnop}\nnopeus on {self.ATMnop}\nkokonaismatka {self.Kmatka}")
        return
#pääohjelma
auto1=Auto("ABC-123",142, "", "" )
