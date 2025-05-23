from Ocena import Ocena
from Uczen import Uczen
from Obecnosc import Obecnosc


#TODO - koniecznie metoda do zwracania ucznia po PESEL-u
class Dziennik:
    def __init__(self):
        self.dziennik = [] #Tu docelowo umieściłbym słownik, dla "numerków", ale nie jest to wymagane

    def dodaj_ucznia(self) -> None:
        imie = input("Podaj imię ucznia: ")
        nazwisko = input("Podaj nazwisko ucznia: ")
        pesel = input("Podaj pesel ucznia: ")

        self.dziennik.append(Uczen(imie, nazwisko, pesel))

    def usun_ucznia(self) -> None:
        pesel = input("Podaj pesel ucznia, którego chcesz usunąć: ")

        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                self.dziennik.remove(uczen)

    def edytuj_ucznia(self) -> None:
        pesel = input("Podaj pesel ucznia, którego chcesz edytować: ")

        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                self.dziennik.remove(uczen)
                self.dodaj_ucznia()

    def sprawdz_obenosc(self) -> None:
        for uczen in self.dziennik:
            print(f"Uczeń: {uczen.imie} {uczen.nazwisko}")

            obecnosc = int(input("Podaj obecnosc: 0 - nieobecny, 1 - spozniony, 2 - obecny, 3 - usprawiedliwiony\n"))
            data = input("Podaj datę (fromat: YYYY-MM-DD): ")
            match obecnosc:
                case 0 :
                    uczen.dodaj_obecnosc(data, Obecnosc.Nieobecny)
                case 1:
                    uczen.dodaj_obecnosc(data, Obecnosc.Spozniony)
                case 2:
                    uczen.dodaj_obecnosc(data, Obecnosc.Obecny)

    def wystaw_ocene(self) -> None:
        pesel = input("Podaj pesel ucznia, któremu chcesz wystawić ocenę: ")
        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                # Uczeniowe mogą dostawać oceny za określone prace (kartkówka, sprawdzian, itd), ale nigdzie dalej tego nie potrzebujemy?
                rodzaj = input("Podaj za co jest dana ocena: ")
                ocena = float(input("Podaj ocenę: "))
                data = input("Podaj datę (fromat: YYYY-MM-DD): ")

                uczen.dodaj_ocene(Ocena(rodzaj, ocena, data))

    def edytuj_ocene(self) -> None:
        pesel = input("Podaj pesel ucznia, któremu chcesz edytować ocenę: ")
        data = input("Podaj datę, za kiedy chcesz edytować uczniowy ocenę: ")
        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                for ocena in uczen.oceny:
                    if ocena.data == data:
                        ocena.ocena = float(input("Podaj nową ocenę: "))

    def edytuj_obecnosc(self) -> None:
        pesel = input("Podaj pesel ucznia, któremu chcesz edytować obecność: ")
        data = input("Podaj datę, za kiedy chcesz edytować uczniowy obecność: ")
        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                for obecnosc in uczen.obecnosci:
                    if obecnosc == data:
                        obecnosc.value = int(input("Podaj obecnosc: 0 - nieobecny, 1 - spozniony, 2 - obecny, 3 - usprawiedliwiony\n"))

    def wyswietl_informacje(self) -> None:
        pesel = input("Podaj pesel ucznia, którego chcesz wyświetlić: ")
        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                print(uczen)
                for ocena in uczen.oceny:
                    print(ocena)

    def wystaw_zagrozenie(self) -> None:
        for uczen in self.dziennik:
            liczba_nieobecnosci = 0
            liczba_spoznien = 0
            srednia = Uczen.oblicz_srednia(uczen)

            for obecnosc in uczen.obecnosci.values():
                if  obecnosc == Obecnosc.Nieobecny:
                    liczba_nieobecnosci += 1
                elif obecnosc == Obecnosc.Spozniony:
                    liczba_spoznien += 1

            #Zabawne te ternary są w Pythonie
            uczen.zagrozenie = True if liczba_nieobecnosci > 2 else False
            #Ma być spóźnień na połowie lekcji, trzeba przemyśleć jak liczyć te lekcje
            uczen.zagrozenie = True if liczba_spoznien > 1_000_000 else False
            uczen.zagrozenie = True if srednia < 3 else False

    def wyswietl_srednia(self):
        pesel = input("Podaj pesel ucznia, którego średnią chcesz wyświetlić: ")
        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                srednia = uczen.oblicz_srednia()
                print(srednia)

    def wysiwietl_status(self):
        pesel = input("Podaj pesel ucznia, którego status chcesz wyświetlić: ")
        for uczen in self.dziennik:
            if uczen.pesel == pesel:
                print(uczen.zagrozenie)



