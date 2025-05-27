import datetime
import sys

import Klasa
import Tests
from CUI import *
from Klasa import Klasa
from Obecnosc import Obecnosc
from Uczen import Uczen
from Ocena import Ocena


wybrana_klasa : Klasa = None

def wyswietl_klase():
    add_title("klasa " + wybrana_klasa.nazwa)

    if len(wybrana_klasa.uczniowie) == 0:
        add_list_item("*pusta*\n")
        return None
    else:
        lista_peseli = []
        set_indentation(1)
        for idx, uczen in enumerate(wybrana_klasa.uczniowie):
            add_list_item(str(idx) + ". " + wybrana_klasa.uczniowie[uczen].krotki_string())
            lista_peseli.append(uczen)
        add_list_item("")
        return lista_peseli

def dodaj_ucznia():
    add_form_item("imię", str.isalpha)
    add_form_item("nazwisko", str.isalpha)
    add_form_item("PESEL", Uczen.poprawny_pesel)
    try:
        input_data = query_form()
    except ValueError:
        add_list_item("nieprawidłowe dane, uczeń nie został dodany\n")
        query_cui("potwierdź")
        return

    wybrana_klasa.dodaj_ucznia(Uczen(input_data[0], input_data[1], input_data[2]))

def sprawdz_liste():
    lista_peseli = list(wybrana_klasa.uczniowie.keys())
    for pesel in lista_peseli:
        add_form_item(wybrana_klasa.uczniowie[pesel].krotki_string())

    dzis = datetime.date.today()
    obecnosci = query_form()
    for idx, pesel in enumerate(lista_peseli):
        obecnosc : Obecnosc = Obecnosc.ze_skrotu(obecnosci[idx])
        wybrana_klasa.uczniowie[pesel].obecnosci[dzis] = obecnosc

def dodaj_oceny():
    add_form_item("komentarz")
    add_list_item("\n")

    lista_peseli = list(wybrana_klasa.uczniowie.keys())
    for pesel in lista_peseli:
        add_form_item(wybrana_klasa.uczniowie[pesel].krotki_string(), Ocena.walidacja)
    oceny = query_form(nothrow = True)

    dzis = datetime.date.today()
    for idx, pesel in enumerate(lista_peseli, start = 1):
        if len(oceny[idx]) > 0:
            try:
                wybrana_klasa.wystaw_ocene(pesel, oceny[0], float(oceny[idx]), dzis)
            except ValueError:
                pass

def wybierz_ocene() -> (list, int):
    lista_peseli = wyswietl_klase()
    numer_ucznia = query_cui()

    set_indentation(1)
    add_title("lista ocen")
    oceny = wybrana_klasa.uczniowie[lista_peseli[numer_ucznia]].oceny
    for idx, ocena in enumerate(oceny):
        add_list_item(str(idx) + '. ' + ocena.__str__())

    numer_oceny = query_cui()
    return oceny, numer_oceny

def edytuj_oceny():
    oceny, numer_oceny = wybierz_ocene()

    while True:
        set_indentation(1)
        add_title("nowe wartości")

        add_form_item("komentarz")
        add_form_item("ocena", Ocena.walidacja)
        add_form_item("data wystawienia (YYYY-MM-DD)")
        try:
            wartosci = query_form()
        except ValueError:
            continue

        oceny[numer_oceny] = Ocena(wartosci[0], float(wartosci[1]), datetime.date.fromisoformat(wartosci[2]))
        break

def usun_ocene():
    oceny, numer_oceny = wybierz_ocene()
    del oceny[numer_oceny]

def menu_edycji_ocen():
    add_option_item("dodaj oceny", dodaj_oceny)
    add_option_item("edytuj istniejącą ocenę", edytuj_oceny)
    add_option_item("usuń ocenę", usun_ocene)
    add_option_item("powrót", lambda: None)
    query_cui_callback()

def wyswietl_szczegoly():
    lista = wyswietl_klase()
    numer = query_cui()
    add_list_item(wybrana_klasa.uczniowie[lista[numer]].__str__())
    try:
        query_cui("enter by wrócić")
    except InterruptedError:
        clear_cui()

def wygeneruj_raport_ucznia():
    lista = wyswietl_klase()
    numer = query_cui()

    uczen = wybrana_klasa.uczniowie[lista[numer]]
    uczen.wygeneruj_raport()
    add_title("raport wygenerowany pomyślnie\n")
    try:
        query_cui("enter by wrócić")
    except InterruptedError:
        clear_cui()

def wygeneruj_wykres_kolowy_frekewencji_ucznia():
    lista = wyswietl_klase()
    numer = query_cui()

    uczen = wybrana_klasa.uczniowie[lista[numer]]
    uczen.wygeneruj_wykres_frekwencji()
    try:
        query_cui("enter by wrócić")
    except InterruptedError:
        clear_cui()

def wygeneruj_histogram_ocen_ucznia():
    lista = wyswietl_klase()
    numer = query_cui()

    uczen = wybrana_klasa.uczniowie[lista[numer]]
    uczen.wygenereuj_wykres_ocen()
    try:
        query_cui("enter by wrócić")
    except InterruptedError:
        clear_cui()

def wygeneruj_wykres_sredniej_klasy():
    klasa = wybrana_klasa
    klasa.wygeneruj_wykres_srednich()
    try:
        query_cui("enter by wrócić")
    except InterruptedError:
        clear_cui()

def powrot() -> None:
    raise InterruptedError

def wybor_klasy():
    global wybrana_klasa
    wybrana_klasa = None
    while wybrana_klasa is None:
        for klasa in Klasa.lista_klas():
            add_option_item(klasa.nazwa)
        try:
            wybrana_klasa = Klasa.lista_klas()[query_cui()]
        except InterruptedError:
            clear_cui()
            continue

    while True:
        wyswietl_klase()
        set_indentation(0)
        add_option_item("edytuj oceny", menu_edycji_ocen)
        add_option_item("sprawdź listę obecności", sprawdz_liste)
        add_option_item("dodaj ucznia do klasy", dodaj_ucznia)
        add_option_item("szczegóły ucznia", wyswietl_szczegoly)
        add_option_item("wygeneruj raport ucznia", wygeneruj_raport_ucznia)
        add_option_item("wygeneruj wykres frekwencji ucznia", wygeneruj_wykres_kolowy_frekewencji_ucznia)
        add_option_item("wygeneruj wykres ocen ucznia", wygeneruj_histogram_ocen_ucznia)
        add_option_item("wygeneruj wykres średniej klasy", wygeneruj_wykres_sredniej_klasy)
        add_option_item("powrót", powrot)
        try:
            query_cui_callback()
        except InterruptedError:
            break


def on_exit():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(0)

Tests.dodaj_dane_testowe()
while True:
    clear_cui()
    add_option_item("wybór klasy", wybor_klasy)
    add_option_item("zamknij program", on_exit)
    query_cui_callback()
