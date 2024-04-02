name = input()
surname = input()
dateOfBirth = input("Podaj w formacie 'dd-mm-rrrr")
email = input()
emailWalidator = email.split("@")
DOBtab = dateOfBirth.split('-')
if int(DOBtab[0]) > 31 or int(DOBtab[0]) < 0:
   print("Bledny dzien")
if int(DOBtab[1]) >12 or int(DOBtab[1]) <0:
    print("Bledny miesiac")
if int(DOBtab[2]) <1900 or int(DOBtab[2]) >2024:
   print("Bledny rok")
if emailWalidator[1].isdigit is True or email.__contains__('.') is not True:
    print("Bledny adres email")

def szyfrowanie_maila(email):
 if "@" in email:
  username,domain = email.split("@")
  username = username[0].upper() +'*' * (len(username) - 1)
  result =f"{username}@{domain}"
  return result
 else :
  return "Bledny adres email"
zaszyfrowanyMail =  szyfrowanie_maila(email)
print(zaszyfrowanyMail)
def szyfrowanie_imie_nazwisko(name,surname):
 surname= surname[0].upper() +'*' * (len(surname)-1)
 name=name[0].upper() +'*' * (len(name)-1)
 result = f"{name}+' '{surname}"
 return result
zaszyfrowaneDane= szyfrowanie_imie_nazwisko(name,surname)
import datetime
from datetime import datetime
date_of_birthDT = datetime.strptime(dateOfBirth, "%d-%m-%Y")
currentDate= datetime.now()

age = currentDate.year-date_of_birthDT.year
dane = {"Imie i nazwisko": zaszyfrowaneDane,"wiek":age,"adres email": zaszyfrowanyMail}
print(dane)