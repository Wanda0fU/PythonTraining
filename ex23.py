nom_fournisseur = input("Donner le nom de fournisseur : ")
n_produit = int(input("Donner le nombre des produits : "))

prix_sup_200 = 0
prix_inf_200 = 0

for i in range(1, n_produit + 1):
    print("Donner le prix Numero ",i,": ",end="")
    prix = float(input(""))
    
    if prix > 200:
        prix_sup_200 += 1
    else:
        prix_inf_200 += 1

print("\nNombre de produits avec un prix > 200 :", prix_sup_200)
print("Nombre de produits avec un prix < 200 :", prix_inf_200)

print("\nNom Fournisseur :", nom_fournisseur)
print("Nombre de Produits :", n_produit)
