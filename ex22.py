nom = input("Donner Votre Nom : ")
filiere = input("Donner Votre Filiere : ")
somme = 0

for n in range (10):
    print("Donner Note Numero",n,":",end=" ")
    n1 = float(input(""))
    somme +=n1

moyenne = somme/10

print("----------------------------------------------")
print("Nom : ",nom)
print("Filiere : ",filiere)
print("----------------------------------------------")
print("Somme = ",somme)
print("Moyenne = ",moyenne)