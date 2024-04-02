typDzialania = input("Napisz jakie dzialanie chcesz wykonac w formacie +,-,/,*")
dzialania = ["+","-","/","*"]


while typDzialania not in dzialania:
  typDzialania = input("Napisz jakie dzialanie chcesz wykonac w formacie +,-,/,*")
  if typDzialania in dzialania:
   break
  
print( typDzialania)
Dane= input("Podaj dane oddzielone przcinkiem")
DaneTab= Dane.split(",")
while DaneTab[0].isnumeric() is False or DaneTab[1].isnumeric() is False:
  Dane = input("Podaj jeszcze raz poprane dane")
  DaneTab= Dane.split(",")
  if DaneTab[0].isnumeric() and DaneTab[1].isnumeric() is True:
   break