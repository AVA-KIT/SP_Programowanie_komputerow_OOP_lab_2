class Konta:
    def __init__(self, imie, nazwisko, numer, nazwa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer
        self.nazwa = nazwa
    def info(self):
        print('Informacja o koncie. ', 
              'Właściciel: ', self.imie, self.nazwisko, self.nazwa,
              ' numer konta: ', self.numer)


class KontoPrywatne(Konta):
    def __init__(self, imie, nazwisko, numer):
        super().__init__(imie, nazwisko, numer, '')
        super().info() #Wypisuje dane podstawowe kont prywatnych
    def zapisPlik(self):
        with open (f'{self.imie}{self.nazwisko}.txt', 'w' ) as plik :
            plik.write(f"{self.imie} {self.nazwisko} numer konta (dane z pliku): {self.numer}")
    def odczytPlik(self):
        with open (f'{self.imie}{self.nazwisko}.txt', 'r' ) as plik :
            konto_plik = plik.read()
            return konto_plik

class KontoFirmowe(Konta):
    def __init__(self, numer, nazwa, zus, pit):
        super().__init__( '' , '', numer, nazwa)
        self.zus = zus
        self.pit = pit
        super().info() #Wypisuje dane podstawowe kont firmowych
    def placeZUS(self):
        print('Płacę ZUS w wysokosci: ', self.zus, ' zł')
    def placePIT(self):
        print('Płacę PIT w wysokosci: ', self.pit, ' zł')
    def zapisPlik(self):
        with open (f'{self.nazwa}.txt', 'w' ) as plik :
            plik.write(f"{self.nazwa} numer konta (dane z pliku): {self.numer}")
    def odczytPlik(self):
        with open (f'{self.nazwa}.txt', 'r' ) as plik :
            konto_plik = plik.read()
            return konto_plik
    
class TaxInfo(Konta):
    def __init__(self, nazwa, kwota, nrkonta):
        super().__init__( '' , '', '', nazwa)
        self.kwota = kwota
        self.nrkonta = nrkonta

class ZusInfo(TaxInfo):
    def __init__(self, nazwa, kwota, nrkonta):
        super().__init__(nazwa, kwota, nrkonta)
    def infoZus(self):
        print(f"Kwota na ZUS wynosi: {self.kwota}")
        print(f"Numer konta do przelewu ZUS: {self.nrkonta}")

class PitInfo(TaxInfo): 
    def __init__(self, nazwa, kwota, nrkonta):
        super().__init__(nazwa, kwota, nrkonta)
    def infoPit(self):
        print(f"Kwota na PIT wynosi: {self.kwota}")
        print(f"Numer konta do przelewu PIT: {self.nrkonta}")

print('--------------------------------')

#Obiekty kont prywatnych
zenek = KontoPrywatne('Zenek', 'Nowak', '123412345667790')
franek = KontoPrywatne('Franek', 'Mocny', '12345634567899344')
janek = KontoPrywatne('Janek', 'Wolny', '12345623456778900')

print('--------------------------------')

#Obiekty kont firmowych
intel = KontoFirmowe('12345446646464456', 'Intel', '12356', '55568')
dell = KontoFirmowe('1754477677447445655', 'Dell', '95686', '88678')
samsung = KontoFirmowe('128903453356734455', 'Samsung', '65997', '10457')

print('--------------------------------')

intel_zus = ZusInfo('Intel', '12356', '134567891026272672')
intel_pit = PitInfo('Intel', '55568', '878865567653235788')
dell_zus = ZusInfo('Dell', '95686', '134567891044566777')
dell_pit = PitInfo('Dell', '88678', '878865567345678899')
samsung_zus = ZusInfo('Samsung', '65997', '13456789155675679')
samsung_pit = PitInfo('Samsung', '10457', '878865567322323456')

lista_zusinfos = []
lista_zusinfos.append(intel_zus)
lista_zusinfos.append(dell_zus)
lista_zusinfos.append(samsung_zus)

for zusinfo in lista_zusinfos:
    print(zusinfo.nazwa)
    zusinfo.infoZus()

print('--------------------------------')

lista_pitinfos = []
lista_pitinfos.append(intel_pit)
lista_pitinfos.append(dell_pit)
lista_pitinfos.append(intel_pit)

for pitinfo in lista_pitinfos:
    print(pitinfo.nazwa)
    pitinfo.infoPit()


lista_kont_firmowych = []
lista_kont_firmowych.append(intel)
lista_kont_firmowych.append(dell)
lista_kont_firmowych.append(samsung)

print('--------------------------------')

#Płacenie należności z kont firmowych
for konto in lista_kont_firmowych:
    print(konto.nazwa)
    konto.placeZUS()
    konto.placePIT()

print('--------------------------------')

zenek.zapisPlik()
print(zenek.odczytPlik())
franek.zapisPlik()
print(franek.odczytPlik())
janek.zapisPlik()
print(janek.odczytPlik())


print('--------------------------------')

intel.zapisPlik()
print(intel.odczytPlik())
dell.zapisPlik()
print(dell.odczytPlik())
samsung.zapisPlik()
print(samsung.odczytPlik())