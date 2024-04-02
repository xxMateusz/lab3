
figura = ["prostokat","trapez","kolo"]
print(f"wybierz jedna z figur{figura}")

figuraUzytkownika = input()
print(figuraUzytkownika)
while figuraUzytkownika not in figura:
     figuraUzytkownika1=input()
     if figuraUzytkownika1 in figura:
          print("figura jest ok ")
          break
     elif figuraUzytkownika1 not in figura :
      input(f"Podaj poprawna figure ")

dane = input("podaj wymiary figury: bok wysokosc i promien jesli jest wymagana")
wymiary = dane.split(',')
if figuraUzytkownika in figura and figuraUzytkownika== figura[0]:
    if len(wymiary)!= 2 :
       while len(wymiary) != 2:
         dane= input("podaj poprawne wymiary prostkata:")
         wymiary1 = dane.split(',')
         if len(wymiary1) == 2:
                print(f"pole prostokata wynosi {int(wymiary1[0]) * int(wymiary1[1])}")
                break    
    elif len(wymiary) ==2:
       print(f"pole prostokata wynosi {int(wymiary[0]) * int(wymiary[1])}")


elif figuraUzytkownika == figura[1]:
    if len(wymiary)!= 3 :
         while len(wymiary) != 3:
          dane= input("podaj poprawne wymiary trapezu w kolejnosci a,b,h:")
          wymiary1 = dane.split(',')
          if len(wymiary1) == 3:
                print(f"pole trapezu wynosi {(int(wymiary1[0]) + int(wymiary1[1]))* int(wymiary1[2]) * 1/2}")
                break    
    elif len(wymiary) ==3:
          print(f"pole trapezu wynosi {(int(wymiary[0]) + int(wymiary[1]))* int(wymiary[2]) * 1/2}")
    
elif figuraUzytkownika == figura[2]:
    if len(wymiary)!= 1 :
         while len(wymiary) != 1:
          dane= input("podaj poprawne wymiary kola czyli r")
          wymiary1 = dane.split(',')
          if len(wymiary1) == 1:
                print(f" pole kola wynosi {int(wymiary[0]) *int(wymiary[0]) * 3.14 }")
                break    
    elif len(wymiary) ==1:
         print(f" pole kola wynosi {int(wymiary[0]) *int(wymiary[0]) * 3.14 }")
    print(f" pole kola wynosi {int(wymiary[0]) *int(wymiary[0]) * 3.14 }")
