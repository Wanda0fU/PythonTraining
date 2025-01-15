nom = input("Donner Votre Nom : ")
mb = float(input("Donner montant brute : "))
d = float(input("Donner la distination : "))
FT = d * 5
if mb > 1500 :
    if d < 100 :
        FTC = 0
        FTS = FT
    else :
        FTC = FT*2/100
        FTS = FT*75/100
else :
    if d < 100 :
        FTC = FT*50/100
        FTS = FT*50/100
    else :
        FTC = FT*75/100
        FTS = FT*25/100
np = mb + FTC
print(nom)
print(mb)
print(np)
print(d)
print(FT)
print(FTC)
print(FTS)