
def rysuj_trojkat(poziomy):
    for i in range(1, poziomy + 1):
        print('*' * i)

# Przykładowe użycie funkcji
poziomy = int(input("Podaj liczbę poziomów trójkąta: "))
rysuj_trojkat(poziomy)
