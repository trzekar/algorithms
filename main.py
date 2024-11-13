import random

# Zadanie 1

def czy_anagramy(slowo1, slowo2):
    return sorted(slowo1) == sorted(slowo2)


slowo1 = "klasa"
slowo2 = "laska"
print(czy_anagramy(slowo1, slowo2))

# Drugą metodą jest zliczanie pętlą

# Zadanie 2

def znajdz_lidera(tablica):
    lider = None
    licznik = 0

    for liczba in tablica:
        if licznik == 0:
            lider = liczba
            licznik = 1
        elif liczba == lider:
            licznik += 1
        else:
            licznik -= 1

    wystapienia = 0
    for liczba in tablica:
        if liczba == lider:
            wystapienia += 1
    

    if wystapienia > len(tablica) // 2:
        return lider
    else:
        return None


# tablica = [1, 1, 2, 2, 2, 2, 1, 2, 3, 2, 2, 4]

tablica = [random.randint(1, 10) for i in range(random.randint(5, 10))]

print("Tablica:", tablica)
print("Lider:", znajdz_lidera(tablica))

# Zadanie 3

def znajdz_idola(tablica):
    n = len(tablica)
    idol = 0
    

    for i in range(1, n):
        if tablica[idol][i] == 1:
            idol = i
    
    for i in range(n):
        if i != idol and (tablica[idol][i] == 1 or tablica[i][idol] == 0):
            return None
    return idol


tablica = [
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]
for wiersz in tablica:
    print(wiersz)
print("Idol:", znajdz_idola(tablica))


# Zadanie 4


def znajdz_maksimum(tablica):
    maksimum = tablica[0][0]
    for wiersz in tablica:
        for liczba in wiersz:
            if liczba > maksimum:
                maksimum = liczba
    return maksimum


n = 4
tablica = [[random.randint(1, 100) for i in range(n)] for i in range(n)]

for wiersz in tablica:
    print(wiersz)
print("Maksimum:", znajdz_maksimum(tablica))





