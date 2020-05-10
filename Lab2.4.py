class Konto():
    def __init__(self, nr_konta, saldo):
        self.nr_konta = nr_konta
        self.saldo = saldo

    def przelew_uznanie(self, kwota):
        self.saldo += kwota

    def przelew_obciazenie(self, kwota):
        if self.saldo - kwota < 0:
            print('Nie masz wystarczających środków aby dokonać przelewu!')
        else:
            self.saldo -= kwota
        
class Obrotowe(Konto):
    def __init__(self, nr_konta, saldo = 10000):
        super().__init__(nr_konta, saldo)

    def uznanie(self, kwota):
        super().przelew_uznanie(kwota)

    def obciazenie(self, kwota):
        super().przelew_obciazenie(kwota)

    def zapisPlik(self):
        with open (f'{self.nr_konta}.txt', 'w' ) as plik :
            plik.write(f"numer konta: {self.nr_konta}, saldo: {self.saldo}")
    def odczytPlik(self):
        with open (f'{self.nr_konta}.txt', 'r' ) as plik :
            konto_plik = plik.read()
            return konto_plik

class Oszczednosciowe(Konto):
    
    przelewy = 0
    miesiace = []
    def __init__(self, nr_konta, saldo = 35000):
        super().__init__(nr_konta, saldo)

    def uznanie(self, kwota):
        super().przelew_uznanie(kwota)   

    def obciazenie(self, kwota):
        super().przelew_obciazenie(kwota)
        Oszczednosciowe.przelewy += 1

    def nastepny_miesiac(self, miesiac):
        Oszczednosciowe.miesiace.append(miesiac)  

    def naliczanie_odsetek(self, odsetki = 5.55):
        if Oszczednosciowe.przelewy > 1 and miesiac not in Oszczednosciowe.miesiace:
            self.saldo -= odsetki

    def zapisPlik(self):
        with open (f'{self.nr_konta}.txt', 'w' ) as plik :
            plik.write(f"numer konta: {self.nr_konta}, saldo: {self.saldo}")
    def odczytPlik(self):
        with open (f'{self.nr_konta}.txt', 'r' ) as plik :
            konto_plik = plik.read()
            return konto_plik

class WykonajPrzelew(Obrotowe, Oszczednosciowe):
    @classmethod
    def przelew(cls, konto_obc, konto_uzn, kwota):
        konto_obc.obciazenie(kwota)
        konto_uzn.uznanie(kwota)

obr_1 = Obrotowe(123)
obr_2 = Obrotowe(124)
obr_3 = Obrotowe(125)
osz_1 = Oszczednosciowe(234)
osz_2 = Oszczednosciowe(235)
osz_3 = Oszczednosciowe(236)
WykonajPrzelew.przelew(obr_1, osz_1, 500)
WykonajPrzelew.przelew(obr_2, osz_3, 260)
WykonajPrzelew.przelew(obr_3, osz_2, 450)
WykonajPrzelew.przelew(osz_1, obr_2, 167)
WykonajPrzelew.przelew(osz_2, osz_3, 300)
WykonajPrzelew.przelew(obr_2, osz_1, 367)

obr_1.zapisPlik()
print(obr_1.odczytPlik())
obr_2.zapisPlik()
print(obr_2.odczytPlik())
obr_3.zapisPlik()
print(obr_3.odczytPlik())
osz_1.zapisPlik()
print(osz_1.odczytPlik())
osz_2.zapisPlik()
print(osz_2.odczytPlik())
osz_3.zapisPlik()
print(osz_3.odczytPlik())
 