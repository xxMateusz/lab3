
figura = ["prostokat","trapez","kolo"]
print(f"wybierz jedna z figur{figura}")
figuraUzytkownika = input()
dane = input("podaj wymiary figury: bok wysokosc i promien jesli jest wymagana")
wymiary = dane.split(' ')
if figuraUzytkownika in figura:
   if figuraUzytkownika == figura[0]:
    print(f"pole prostokata wynosi {int(wymiary[0]) * int(wymiary[1])}")
   elif figuraUzytkownika == figura[1]:
    print(f"pole trapezu wynosi {(int(wymiary[0]) + int(wymiary[1]))* int(wymiary[2]) * 1/2}")
   elif figuraUzytkownika == figura[2]:
    print(f" pole kola wynosi {int(wymiary[2]) *int(wymiary[2]) * 3.14 }")

else :
 print("bledna nazwa figury")
