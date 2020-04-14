class Zwierze:
    def __init__(self, imie, odglos):
        self.imie = imie
        self.odglos = odglos

class Pies(Zwierze):
    def __init__(self, imie, odglos):
        super().__init__(imie, odglos)
    def daj_glos(self):
        print('Jestem psem: ',self.odglos, ' nazywan się : ', self.imie)

class Kot(Zwierze):
    def __init__(self, imie, odglos):
        super().__init__(imie, odglos)
    def daj_glos(self):
        print('Jestem kotem ', self.odglos, ' nazywan się : ', self.imie)

class Kanarek(Zwierze):
    def __init__(self, imie, odglos):
        super().__init__(imie, odglos)
    def daj_glos(self):
        print('Jestem kanarkiem ', self.odglos, ' nazywan się : ', self.imie)
class Kura(Zwierze):
    def __init__(self, imie, odglos):
        super().__init__(imie, odglos)
    def daj_glos(self):
        print('Jestem kurą', self.odglos + ' nazywan się : ', self.imie)

pies = Pies('Azor','HauHau')
kot = Kot('Mruczek','MiałMiał')
kanarek = Kanarek('Ćwirek','ĆwirĆwir')
kura = Kura('Klara','KoKoKo')

lista_zwierzat = [pies, kot, kanarek, kura]

lista_zwierzat[0].daj_glos()
lista_zwierzat[1].daj_glos()
lista_zwierzat[2].daj_glos()
lista_zwierzat[3].daj_glos()