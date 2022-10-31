class Hissi:
    def __init__ (self, ak, yk):
        self.alinkerros=ak
        self.ylinkerros=yk
        self.kerros=0

    def siirry_kerrokseen(self,käsky):
        while käsky != self.kerros:
            if self.kerros< käsky:
                hissi1.kerros_ylös(käsky)
            if self.kerros> käsky:
                hissi1.kerros_alas(käsky)
        return
    def kerros_ylös(self,käsky):
        self.kerros = self.kerros + 1
        print(f'Olet kerroksessa {self.kerros}')
        return
    def kerros_alas(self, käsky):
        self.kerros = self.kerros - 1
        print(f'Olet kerroksessa {self.kerros}')
        return
#pääohjelma

hissi1=Hissi(0,20)
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(0)
