wydatkiRoczne = {"styczen":3400, "luty":4000, "marzec": 3500,"kwiecien":4100, "maj":3800,"czerwiec": 3200,"lipiec":3000,"sierpien": 3300,"wrzesien":3500,"pazdniernik":2900,"listopad":3200,"grudzien":3400}
wartoscMinimalna = min(wydatkiRoczne.values())
print(wartoscMinimalna)
wartoscMaksymalna = max(wydatkiRoczne.values())
print(wartoscMaksymalna)
suma = sum(wydatkiRoczne.values())
print(suma)
srednia = suma/len(wydatkiRoczne)
print(srednia)
if wydatkiRoczne.get("grudzien") > srednia:
    print("zacznij oszczedzac")
else :
    print("jestes bezpieczny")

