import os

option_items : list = []
header = "DZIENNIK OCEN"
indentation = 0

def clear_display():
    global indentation
    indentation = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print(header, end = "\n\n")

def clear_cui():
    clear_display()
    option_items.clear()

def add_option_item(text : str, item : any = None) -> None:
    print('\t' * indentation + str(len(option_items)) + ' ' + text)
    option_items.append(item)

def add_form_item(text : str) -> None:
    option_items.append(text)

def __query_common(prompt : str) -> int:
    user_input = input(prompt)
    if len(user_input) == 0:
        raise InterruptedError

    return int(user_input)

#daje użytkownikowi wybór spośród opcji dostarczonych przez add_option_item i zwraca wybrany indeks
def query_cui(prompt : str = "Wybór: ") -> int:
    user_input = __query_common(prompt)
    clear_cui()
    return user_input

#daje użytkownikowi wybór spośród opcji dostarczonych przez add_option_item zakładając, że są to callbacki, po czym przekazuje kontrolę do wybranego callbacku
def query_cui_callback(prompt : str = "Wybór: ") -> None:
    option_idx = __query_common(prompt)
    callback = option_items[option_idx]
    clear_cui()
    callback()

#traktuje pola dodane przez add_form_item jako kolejne pola formularza, a po wypełnieniu przez użytkownika zwraca listę stringów z wartościami pól
def query_form() -> list:
    option_count = len(option_items)
    if option_count == 1:
        return list(input(option_items[0] + ": "))

    fields_done = 0
    fields_values = list()
    while fields_done < option_count:
        clear_display()
        for i in range(fields_done):
            print(option_items[i] + ': ' + fields_values[i])

        for i in range(option_count - fields_done):
            print(option_items[i + fields_done] + ": ")

        fields_values.append(input('\n' + option_items[fields_done] + ": "))
        fields_done = fields_done + 1

    clear_cui()
    return fields_values


def set_indentation(indent_level : int) -> None:
    global indentation
    indentation = indent_level

def add_title(title : str) -> None:
    print('\t' * (indentation - 1) + title)

def add_list_item(text : str) -> None:
    print('\t' * indentation + text)
