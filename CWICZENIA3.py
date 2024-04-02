def trapezoid(a,b,h):
    print((a+b) *h/2)

trapezoid(1,2,3)

def bmi (kg, h):
 if h >100:
    h /=100
    return kg/(h**2)

def bmi_verdict(bmi):
    if bmi<18.5:
     return ("niedzowaga")
    elif bmi >18.5 and bmi < 25:
     return "wafga prawdiwlowa"
    else :
        return"nadwaga"


human_bmi = (bmi_verdict(bmi(185,80)))
