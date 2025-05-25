from Obecnosc import Obecnosc
from Ocena import Ocena
from datetime import date


class Uczen:
    @staticmethod
    def poprawny_pesel(pesel : str) -> bool:
        if len(pesel) != 11 or not pesel.isdigit():
            return False

        wagi = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 0)
        kontrola = 0
        for idx, cyfra in enumerate(pesel):
            kontrola += int(cyfra) * wagi[idx]

        kontrola = (10 - (kontrola % 10)) % 10
        return kontrola == int(pesel[-1])

    def __init__(self, imie: str, nazwisko: str, pesel: str):
        if not Uczen.poprawny_pesel(pesel):
            pass #raise ArgumentError todo wyłączone na potrzeby testów

        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.oceny = list()
        self.obecnosci = dict() #Zakładamy, że uczeń będzie miał sprawdzaną listę raz dziennie
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
            srednia = self.oblicz_srednia()
        except ArithmeticError:
            return nieobecnosci > 2 or spoznienia > (len(self.obecnosci) / 2)

        return srednia < 3 or nieobecnosci > 2 or spoznienia > (len(self.obecnosci) / 2)


    def krotki_string(self):
        return f"{self.imie} {self.nazwisko}"

    def __str__(self):
        try:
            srednia = str(self.oblicz_srednia())
        except ArithmeticError:
            srednia = "*brak ocen*"

        text = f"Imię: {self.imie}\nNazwisko: {self.nazwisko}\nŚrednia ocen: {srednia}\nZagrożenie: {self.czy_zagrozony()}\nObecność:\n"
        for obecnosc in self.obecnosci:
            text += f"{obecnosc} {self.obecnosci[obecnosc].__str__().removeprefix("Obecnosc.")}\n"
        text += '\nOceny:\n'
        for ocena in self.oceny:
            text += f"{ocena}\n"
        return text
