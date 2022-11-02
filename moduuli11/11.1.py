class julkaisu:
    def __init__(self, nimi):
        self.nimi=nimi

    def tulosta_tiedot(self):
        print(self.nimi)

class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja=kirjoittaja
        self.sivumäärä=sivumäärä
        super(kirja, self).__init__(nimi)

    def tulosta_tiedot(self):
        super(kirja, self).tulosta_tiedot()
        print(f"Kirjan tiedot {self.kirjoittaja, self.sivumäärä}")

class lehti(julkaisu):
    def __init__(self,nimi,päätoimittaja):
        self.päätoimittaja=päätoimittaja
        super(lehti, self).__init__(nimi)

    def tulosta_tiedot(self):
        super(lehti, self).tulosta_tiedot()
        print(f"Lehden tiedot {self.päätoimittaja}")


#pääohjelma
julkaisut=[]
julkaisut.append(lehti("Aku Ankka","Aki Hyyppä"))
julkaisut.append(kirja("Hytti n:o 6", "Rosa Liksmon", 200))

for I in julkaisut:
    I.tulosta_tiedot()