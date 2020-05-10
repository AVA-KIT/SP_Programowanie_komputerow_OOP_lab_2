class Pracownik:
    Wynagrodzenie_pracownika = {
        'P1': '2500 zł',
        'P2': '2750 zł',
        'P3': '3150 zł',
        'P4': '3525 zł'
    }
    
    def __init__(self, imie, nazwisko, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
    
        if wynagrodzenie not in Pracownik.Wynagrodzenie_pracownika:
            raise ValueError(f'Niewłaściwy klucz wynagrodzenia. Dostępne wynagrodzenie: {list(Pracownik.Wynagrodzenie_pracownika)}')
        self.wynagrodzenie = Pracownik.Wynagrodzenie_pracownika[wynagrodzenie]
    
    def wypłata_do_pracownika(self):
        print(f"Pracownik: {self.imie} {self.nazwisko} - wypłata: {self.wynagrodzenie}")

pracownik_1 = Pracownik("Jan", "Kowalski", "P1")
pracownik_1.wypłata_do_pracownika()