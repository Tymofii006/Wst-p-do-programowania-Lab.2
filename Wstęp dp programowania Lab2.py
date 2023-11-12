                             # 1
pierwsza_liczba = int(input("Podaj pirwszą liczbe całkowitą: "))
druga_liczba = int(input("Podaj drugą liczbe całkowitą: "))

if pierwsza_liczba < druga_liczba:
    mniejsza = pierwsza_liczba
    większa = druga_liczba

else:
    mniejsza = druga_liczba
    większa = pierwsza_liczba

print("Liczby od", mniejsza , "do", większa,  "to:")

for liczba in range(mniejsza, większa +1):
    print(liczba)


                             #2
def funkcja_y(x):
    return 2 * x**2 - 5 * x - 8

def main():
    x_poczatek = -4
    x_koniec = 4
    krok = 0.5

    print("x\t\t y")

    x = x_poczatek
    while x <= x_koniec:
        y = funkcja_y(x)
        print(f"{x:.2f}\t\t{y:.2f}")
        x += krok

if __name__ == "__main__":
    main()


                                   #3

while True:
    liczba = int(input("Podaj liczbę całkowitą: "))

    if liczba < 0:
        print("Podano licbę ujemną. Koniec. ")
        break
    else:
        print(f"Podano liczbę dodatnią: {liczba}")



                                    #4 (Zmodyfikowane zadanie 1)

pierwsza_liczba = int(input("Podaj pierwszą liczbę całkowitą: "))
druga_liczba = int(input("Podaj drugą liczbę całkowitą: "))

if pierwsza_liczba < druga_liczba:
    mniejsza = pierwsza_liczba
    większa = druga_liczba
else:
    mniejsza = druga_liczba
    większa = pierwsza_liczba

print("Liczby parzyste od", mniejsza, "do", większa, "to:")

for liczba in range(mniejsza, większa + 1):
    if liczba % 2 != 0:  # Pomija liczby nieparzyste
        continue
    print(liczba)


                                   #5
n = int(input("Podaj liczbę studentów: "))

suma_punktow = 0

i = 1
while i <= n:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i}: "))
    suma_punktow += punkty
    i += 1

srednia = suma_punktow / n

print(f"Średnia liczba punktów w grupie: {srednia}")


                                #6 (Zmodyfikowane 5)
n = int(input("Podaj liczbę studentów: "))
suma_punktow = 0
i = 1

while True:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i}: "))

    if punkty < 0 or punkty > 100:
        print("Liczba punktów spoza przedziału 0-100. Podaj poprawną liczbę.")
        continue

    suma_punktow += punkty
    i += 1

    if i > n:
        break

srednia = suma_punktow / n

print(f"Średnia liczba punktów w grupie: {srednia}")










