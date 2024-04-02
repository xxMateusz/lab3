import math
a = 2
b = 2
c = -12
if a < 0 or b<0 or c<0:
    print("sprawdz podane wartosci, bo sa bledne")
delta = (b*b)-4*(a*c)
print(delta)
x1 = (-b - math.sqrt(delta))/(2*a)
x2 = (-b + math.sqrt(delta))/(2*a)
print(x1)
print(x2)