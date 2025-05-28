from collections import Counter

import matplotlib
import pandas as pd

matplotlib.use('TkAgg') # bez tego rzuca err, rozwiazanie:
# https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/issues/2411

import matplotlib.pyplot as plt
from pandas import ExcelWriter

from argparse import ArgumentError

from Obecnosc import Obecnosc
from Ocena import Ocena
from datetime import date, datetime


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
            raise ArgumentError

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

    def wygeneruj_raport(self) -> None:
        timestamp = datetime.now().timestamp()
        file_name = f"{self.nazwisko}{timestamp}.xlsx"

        df_obecnosci = pd.DataFrame([
            {"Data" : data, "Obecność" : obecnosc.name}
            for data, obecnosc in self.obecnosci.items()
        ])

        df_oceny = pd.DataFrame([
            {"Komentarz" : ocena.rodzaj, "Ocena" : ocena.ocena, "Data" : ocena.data}
            for ocena in self.oceny
        ])

        with ExcelWriter(file_name) as writer:
            df_obecnosci.to_excel(writer, sheet_name='Obecności', index=False, header=True)
            df_oceny.to_excel(writer, sheet_name="Oceny", index=False, header=True)

    def wygeneruj_wykres_frekwencji(self) -> None:
        obenosci = [obecnosc.name for obecnosc in self.obecnosci.values()]
        count = Counter(obenosci)

        label = list(count.keys())
        counter = list(count.values())

        plt.pie(counter, labels=label, autopct='%1.1f%%')
        plt.title(f"Wykres kołowy frekwencji ucznia {self.krotki_string()}")
        plt.tight_layout()
        plt.show()

    def wygenereuj_wykres_ocen(self) -> None:
        oceny = [ocena.ocena for ocena in self.oceny]

        plt.hist(oceny, color='green', rwidth=0.5, range=(2, 6))
        plt.title(f"Histogram ocen ucznia {self.krotki_string()}")
        plt.xlabel("Ocena")
        plt.tight_layout()
        plt.show()

    def krotki_string(self):
        return f"{self.imie} {self.nazwisko}"

    def __str__(self):
        try:
            srednia = str.format('%1.2f' % self.oblicz_srednia())
        except ArithmeticError:
            srednia = "*brak ocen*"

        text = f"Imię: {self.imie}\nNazwisko: {self.nazwisko}\nPESEL: {self.pesel}\nŚrednia ocen: {srednia}\nZagrożenie: {self.czy_zagrozony()}\nObecność:\n"
        for obecnosc in self.obecnosci:
            text += f"{obecnosc} {self.obecnosci[obecnosc].__str__().removeprefix("Obecnosc.")}\n"
        text += '\nOceny:\n'
        for ocena in self.oceny:
            text += f"{ocena}\n"
        return text
