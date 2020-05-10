class Konta:
    def __init__(self, imie, nazwisko, numer, nazwa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer
        self.nazwa = nazwa
    def info(self):
        print('Informacja o koncie. ', 'Właściciel: ', self.imie, self.nazwisko, self.nazwa, ', numer konta: ', self.numer)
    
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
    
print('--------------------------------')

#Obiekty kont prywatnych
zenek = KontoPrywatne('Zenek', 'Nowak', '123412345667790')
franek = KontoPrywatne('Franek', 'Mocny', '12345634567899344')
janek = KontoPrywatne('Janek', 'Wolny', '12345623456778900')

print('--------------------------------')

#Obiekty kont firmowych
intel = KontoFirmowe('12345446646464456', 'Intel', '123567678', '55568556')
dell = KontoFirmowe('1754477677447445655', 'Dell', '956864', '88678554')
samsung = KontoFirmowe('128903453356734455', 'Samsung', '6599766', '10457744')

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