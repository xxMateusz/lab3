pesel = input()
peselInt = list(map(int,pesel))
test = peselInt[2] + peselInt[3]
if len(peselInt) != 11:
    print("Bledna dlugosc numeru pesel")
rokUrodzenia= input("Podaj rok urodzenia")
miesiacUrodzenia= input("Podaj miesiac urodzenia w formie 00")
dzienUrodzenia= input("Podaj dzien urodzenia w formie 00")

rokUrodzeniaInt = list(map(int,rokUrodzenia))
walidacjaRoku = f"{rokUrodzeniaInt[2]}{rokUrodzeniaInt[3]}"
peselRok = f"{peselInt[0]}{peselInt[1]}"

miesiace19xx = {
    "01": "Styczen","02": "Luty","03": "Marzec","04": "Kwiecien","05": "Maj","06": "Czerwiec","07": "Lipiec","08": "Sierpien","09": "Wrzesien","10": "Pazdziernik","11": "Listopad", "12": "Grudzien"
}
miesiace20xx = {"21": "Styczen", "22": "Luty", "23": "Marzec", "24": "Kwiecien", "25": "Maj", "26": "Czerwiec", "27": "Lipiec", "28": "Sierpien", "29": "Wrzesien", "30": "Pazdziernik", "31": "Listopad", "32": "Grudzien"}

print(miesiace19xx)


walidacja1 = f"{peselInt[0]}{peselInt[1]}"
cyfryDlaLat = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
cyfryDlaLat2=['21','22','23','24','25','26','27','28','29','30','31','32']
walidacja2= f"{peselInt[2]}{peselInt[3]}"
peselDni = f"{peselInt[4]}{peselInt[5]}"
dniInt = list(map(int,dzienUrodzenia))
walidacjaDni = f"{dniInt[0]}{dniInt[1]}"
if walidacjaRoku == peselRok:
 print("rok sie zgadza")
 if int(rokUrodzenia)<2000 and walidacja2 in cyfryDlaLat:
  if peselDni==walidacjaDni:
    print("Pesel jest Poprawny")
    if walidacja2 in cyfryDlaLat :
        lata="19"
        if peselInt[10] in [0,2,4,6,8]:
         plec = "Kobieta"
         print(f"{peselDni} {miesiace19xx[walidacja2]} {lata}{walidacja1} plec:{plec}")
        else:
         plec="mezczyna"
         print(f"{peselDni} {miesiace19xx[walidacja2]} {lata}{walidacja1} plec:{plec}")

  else:
     print("bledny dzien lub cyfry 4,5 w peselu")
 
 elif int(rokUrodzenia) >=2000 and walidacja2 in cyfryDlaLat2:
  if peselDni==walidacjaDni:
    print("Pesel jest Poprawny")  
    if walidacja2 in cyfryDlaLat2:
      lata="20"
      if peselInt[10] in [0,2,4,6,8]:
         plec = "Kobieta"
         print(f"{peselDni} {miesiace20xx[walidacja2]} {lata}{walidacja1} plec:{plec}")
      else:
         plec="mezczyna"
         print(f"{peselDni} {miesiace20xx[walidacja2]} {lata}{walidacja1} plec:{plec}")

 else :
  print("Bledny pesel lub rok urodzenia")
else :print("bledny rok lub pesel")