class Talo:
    def __init__ (self,ak,yk,LKM):
        self.alinkerros=ak
        self.ylinkerros=yk
        self.hissitLKM=LKM
        self.hissilista=[]
        for i in range(self.hissitLKM):
            self.hissilista.append(Hissi(ak,yk))
    def aja_hissiä(self,numero, kohde):
        self.hissinnumero=numero
        self.kohdekerros=kohde
        self.hissilista[numero].siirry_kerrokseen(kohde)
    def palohälytys(self):
        for I in range(len(self.hissilista)):
            self.aja_hissiä(I,self.alinkerros)

class Hissi:
    def __init__ (self, ak, yk):
        self.alinkerros=ak
        self.ylinkerros=yk
        self.kerros=0

    def siirry_kerrokseen(self,käsky):
        while käsky != self.kerros:
            if self.kerros< käsky:
                self.kerros_ylös()
            if self.kerros> käsky:
                self.kerros_alas()
        return
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(f'Olet kerroksessa {self.kerros}')
        return
    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(f'Olet kerroksessa {self.kerros}')
        return
#pääohjelma
#talon tiedot
talo1=Talo(0,20,4 )
talo1.aja_hissiä(1,4)
talo1.aja_hissiä(2,4)
talo1.palohälytys()
