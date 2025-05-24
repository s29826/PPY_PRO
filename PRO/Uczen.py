from Obecnosc import Obecnosc
from Ocena import Ocena
from datetime import date


class Uczen:
    def __init__(self, imie: str, nazwisko: str, pesel: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.oceny = list()
        #Zakładam, że uczeń będzie miał sprawdzaną listę raz dziennie
        self.obecnosci = dict()
        self.zagrozenie = False

    def dodaj_obecnosc(self, data: date, obecnosc: Obecnosc) -> None:
        self.obecnosci[data] = obecnosc

    def dodaj_ocene(self, ocena: Ocena) -> None:
        self.oceny.append(ocena)

    def oblicz_srednia(self) -> float:
        if len(self.oceny) == 0:
            raise ArithmeticError

        suma_ocen = 0

        for ocena in self.oceny:
            suma_ocen += ocena.ocena

        return suma_ocen / len(self.oceny)

    def czy_zagrozony(self) -> bool:
        nieobecnosci = sum(1 for value in self.obecnosci.values() if value == Obecnosc.Nieobecny)
        spoznienia = sum(1 for value in self.obecnosci.values() if value == Obecnosc.Spozniony)
        srednia : float
        try:
            srednia = self.oblicz_srednia() < 3
        except ArithmeticError:
            return nieobecnosci > 2 or spoznienia > (len(self.obecnosci) / 2)

        return srednia < 3 or nieobecnosci > 2 or spoznienia > (len(self.obecnosci) / 2)


    def krotki_string(self):
        return f"{self.imie} {self.nazwisko}"

    def __str__(self):
        return f"Imię: {self.imie}\nNazwisko: {self.nazwisko}\nObecność: {self.obecnosci}\nOceny: {self.oceny}\nZagrożenie: {self.czy_zagrozony()}"
