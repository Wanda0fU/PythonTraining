nom_fournisseur = input("Donner le nom de fournisseur : ")
n_operation = int(input("Donner le nombre des opérateurs : "))

total = 0
nombre_solde = 0
nb_sold_sup = 0
nb_sold_inf = 0
solde_max = float('-inf')
solde_min = float('inf')

for i in range(1, n_operation + 1):
    print("Donner le solde", i, ": ", end="")
    solde = int(input())
    total += solde
    nombre_solde += 1
    

    if solde > solde_max:
        solde_max = solde
    if solde < solde_min:
        solde_min = solde

    moyenne = total / nombre_solde
    if solde > 1000:
        nb_sold_sup += 1
    else:
        nb_sold_inf += 1
    if solde < 0:
        print("Erreur !")
        break
print("\n-----------------------------------------------------------")
print("             Nom du fournisseur :", nom_fournisseur)
print("             Nombre de soldes entrés :", nombre_solde)
print("-----------------------------------------------------------")
print("             Total des soldes :", total)
print("             Moyenne des soldes :", moyenne)
print("-----------------------------------------------------------")
print("             Solde maximum :", solde_max)
print("             Solde minimum :", solde_min)
print("-----------------------------------------------------------")
print("             Nombre de soldes supérieurs à 1000 :", nb_sold_sup)
print("             Nombre de soldes inférieurs à 1000 :", nb_sold_inf)
print("-----------------------------------------------------------")