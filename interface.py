import sys
import time
from drzewa_final import *

root = None
my_tree = Tree()



def starting():
    while True:
        try:
            print("Poszę pdoać maksymalnie 10 cyfr "
                                 "naturalnych całkowitych, odzielonych spacjiami.")
            user_input = input("Twoje cyfry:")
            if user_input == "ESC":
                return -1
            to_make = list(map(int, user_input.split()))
        except ValueError:
            print(to_make)
            print("Przynajmiej jeden z elementów nie jest cyfrą! Prosze spróbować jeszcze raz.")
        else:
            work = True
            if len(to_make) > 10:
                print("")
                print("Za dużo cyf! Proszę wprowadzić jeszcze raz.")
                time.sleep(1.5)
                print("")
            for i in to_make:
                if i < 0:
                    print('')
                    print("Liczby powinny być większe od zera! Proszę spróbować jeszcze raz.")
                    time.sleep(1.5)
                    print('')
                    work = False
                    break
            if work == True:
                return to_make
def build_tree():
    while True:
        print("")
        answer = input("Które z drzwe chcesz zbudować?\n1.Winorośl\n2.AVL\nTwoja odpowiedź:")
        if answer == '1':
            print("")
            print("Wybrałeś Winrośl")
            return answer
        elif answer == '2':
            print("")
            print("Wybrałeś drzewo AVL")
            return answer
        elif answer == "ESC":
            print("")
            print("Program zostanie zakończony")
            return answer
        elif answer == "BACK":
            print("")
            print("Cofniesz się do wprowadzania danych")
            return answer

        else:
            print("")
            print("Błędna opdowiedź! Proszę spróbować jeszczre raz")
            return answer
def operation_on_tree():
    while True:
        sys.stdout.write("Towje opjce:\n1.Zbalansuj Drzewo\n2.Usuń element\n"
                         "3.Usuń Całe Drzewo\n4.Wyszukaj największy element\n"
                         "5.Wyszukaj najmniejszy elemnt\n6.Wypisz elemnty w porządku in-order\n"
                         "7.Wypisz elemnty w porządku pre-order\n8.Zmień typ drzewa\Zresetuj Drzweo do początkowego stanu.\n")
        choice = input("Podaj numer czynności którą chcesz wykonać: ")
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8'] or choice == "ESC" or choice == "BACK":
            return choice
        else:
            print("Błędna odpowidź! Proszę wprowadzić jeszcze raz.")
def usuwacz():
    global to_make
    global data
    while True:
        try:
            print("")
            ile = input("Proszę podać ilość elemntów które chcesz usnuąć:")
            if ile == "ESC":
                print("")

                print("Program się zakończy")
                time.sleep(0.8)
                return -1
            if ile == "BACK":
                print("")

                print("Usuwanie się zakończy. Powrót do komend.")
                time.sleep(0.8)
                return -2
            ile = int(ile)


        except:
            print('')

            print('Błąd! Proszę wprowadzić poprawne dane')
            time.sleep(0.8)
        else:
            if ile > len(to_make):
                print("")

                print("Podano więcej elemntów do usunięcia niż znajduję się w drzwie. "
                      "Proszę wprowadzić jeszcze raz")
                time.sleep(0.8)

                pass
            else:
                print("")

                el_list = input("Proszę podać wartości odzielone spacjami:")
                if el_list == "ESC":
                    print("")

                    print("Program się zakończy")
                    time.sleep(0.8)

                    return -1
                elif el_list == "BACK":
                    print("")

                    print("Powrót do podawania ilości.")
                    time.sleep(0.8)

                else:
                    try:
                        el_to_del = list(map(int, el_list.split()))
                    except ValueError:
                        print("")

                        print("Błedna odpowieź! Proszę podać cyfry")
                        time.sleep(0.8)

                    else:
                        if ile == len(el_to_del):
                            for i in el_to_del:
                                if i not in to_make:
                                    print("")
                                    print(f"Element ${i} nie znaduję się wśród elementów. Proszę wprowadzić dane jeszcze raz.")
                                    break
                                    print("")
                                    time.sleep(0.8)
                            print("")

                            print("Elemnty zostaną usuniętę. Powrót do komend.")
                            time.sleep(0.8)

                            for i in el_to_del:
                                data = my_tree.delete(data, i)
                            return 0
                        else:
                            print("")
                            print("Ilość do usinięcia nie zgadza się z ilością wprowadzonych danych."
                                  "Proszę sprubować jeszcze raz")
                            time.sleep(0.8)

print('-------------------------------')
print("Aby wyjśc z programu wpisz \'ESC\'")
print("Aby wrócić do poprzednigo kroku wpisz\'BACK\'")
print("Aby wykonać czynność, należy podać jej cyfrę")
print('-------------------------------')

running = True

while running:
    to_make = starting()
    if to_make == -1:
        print("")
        print("Program zostanie zakończony.")
        time.sleep(0.8)
        running = False
    elif len(to_make) == 0:
        print("")
        print("Nie podano rzadnego elementu! Nie można zbudować Drzewa. Proszę sprubować jeszcze raz.")
        print("")

        time.sleep(0.8)

    else:
        to_make.sort()
        making_tree = True
        while making_tree:
            next = False
            answer = build_tree()
            if answer == '1':
                next = True
                data = my_tree.Degeneratmaker(root, to_make, 0, len(to_make) - 1)
            elif answer == '2':
                next = True
                data = my_tree.Avlmaker(root, to_make, 0, len(to_make) - 1)
            elif answer == "ESC":
                making_tree = False
                running = False
            elif answer == "BACK":
                making_tree = False
            if next is True:
                time.sleep(0.8)
                while next is True and running is True:
                    print("")
                    print("Oto twoje Drzweo:")
                    my_tree.printer(data, "", True)
                    choice = operation_on_tree()
                    if choice == '1':
                        print("")
                        print("Twoje drzewo zostanie zbalansowane metodą DSW")
                        print("")
                        time.sleep(0.8)
                        data = my_tree.degenerate(data)
                        data = my_tree.balance(data)
                    if choice == '2':
                        print("")
                        usuwanie = usuwacz()
                        if usuwanie == -1:
                            making_tree = False
                            running = False
                        if usuwanie == -2 or usuwanie == 0:
                            pass
                    if choice == '3':
                        print("")
                        print('Twoje drzewo zostanie usunięte\nNastąpi powrót do podawania dnaych.')
                        print("")
                        time.sleep(0.8)
                        data = my_tree.delete_all(data)
                        next = False
                        making_tree = False
                    if choice == '4':
                        print("")
                        print("Ścieżka:")
                        najmie = my_tree.min_value(data)
                        print("")
                        print("Oto twój najmiejszy element:")
                        print(najmie)
                        print("")
                        time.sleep(0.8)
                    if choice == '5':
                        print("")
                        print("Ścieżka:")
                        najwie = my_tree.max_value(data)
                        print("")
                        print("Oto twój największy element:")
                        print(najwie)
                        print("")
                        time.sleep(0.8)

                    if choice == '6':
                        print("")
                        print("Elementy wypisane w porządku in-order:")
                        my_tree.in_order_search(data)
                        print("")
                        time.sleep(0.8)
                    if choice == '7':
                        print("")
                        print("Elementy wypisane w porządku post-order:")
                        my_tree.pre_order_search(data)
                        print("")
                        time.sleep(0.8)

                    if choice == '8' or choice == "BACK":
                        print("")
                        print("Powrót do wyboru Drzewa.")
                        print("")
                        time.sleep(0.8)
                        next = False
                    if choice == "ESC":
                        print("")
                        print("Program zostanie zakończony.")
                        print("")
                        time.sleep(0.8)

                        running = False
                        next = False
                        making_tree = False
