import datetime
import os
import sys

import Klasa
import Tests
from CUI import *
from Klasa import Klasa
from Obecnosc import Obecnosc
from Uczen import Uczen


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
    add_form_item("imię")
    add_form_item("nazwisko")
    add_form_item("PESEL")
    input_data = query_form()
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
        add_form_item(wybrana_klasa.uczniowie[pesel].krotki_string())
    oceny = query_form()
    dzis = datetime.date.today()
    for idx, pesel in enumerate(lista_peseli, start = 1):
        wybrana_klasa.wystaw_ocene(pesel, oceny[0], float(oceny[idx]), dzis)

def wyswietl_szczegoly():
    lista = wyswietl_klase()
    numer = query_cui()
    add_list_item(wybrana_klasa.uczniowie[lista[numer]].__str__())  #todo dopracować pokazywane dane
    try:
        query_cui("enter by wrócić")
    except InterruptedError:
        clear_cui()

def powrot():
    raise InterruptedError

def wybor_klasy():
    for klasa in Klasa.lista_klas():
        add_option_item(klasa.nazwa)
    global wybrana_klasa
    wybrana_klasa = Klasa.lista_klas()[query_cui()]

    while True:
        wyswietl_klase()
        set_indentation(0)
        add_option_item("dodaj oceny", dodaj_oceny)
        add_option_item("sprawdź listę obecności", sprawdz_liste)
        add_option_item("dodaj ucznia do klasy", dodaj_ucznia)
        add_option_item("szczegóły ucznia", wyswietl_szczegoly)
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
