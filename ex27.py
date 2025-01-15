n_contract = int(input("Donner le numero de contract : "))
n_compteur = int(input("Donner le numero de compteur : "))
nom_client = input("Donner le nom de client : ")
type_client = input("Donner le type de client : ")
mois = input("Donner le mois : ")
an_indice = float(input("Donner l'indice ancien : "))
nv_indice = float(input("Donner l'indice nouveau : "))

consommation = nv_indice - an_indice

if consommation <= 100:
    montant_brute = consommation * 2
elif consommation <= 250:
    montant_brute = (100 * 2) + ((consommation - 100) * 2.5)
else:
    montant_brute = (100 * 2) + (150 * 2.5) + ((consommation - 250) * 3)

if type_client.lower() == "ste" :
    frais = 300
elif type_client.lower() == "personnel" :
    frais = 200
else :
    frais = 150

TVA = montant_brute*20/100
net = montant_brute + TVA + frais

print("\n----------------------------------- Facture d'électricité ---------------------------------------")
print(f"Numéro de contrat : {n_contract}                          Nom du client : {nom_client}")
print(f"Numéro de compteur : {n_compteur}                          Type de client : {type_client}")
print("-----------------------------------------------------------------------------------------")
print(f"Mois : {mois}")
print(f"Indice Ancient : {an_indice}")
print(f"Indice Nouveau : {nv_indice}")
print("-----------------------------------------------------------------------------------------")
print(f"Consommation : {consommation} kWh")
print(f"Montant brut : {montant_brute:.2f} MAD")
print(f"TVA (20%) : {TVA:.2f} MAD")
print(f"Frais fixes : {frais:.2f} MAD")
print(f"Montant net à payer : {net:.2f} MAD")
print("-----------------------------------------------------------------------------------------")