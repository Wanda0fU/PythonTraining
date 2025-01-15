somme = 0
for i in range (1,9):
    print("Donner Nombre",i,": ",end="")
    n = int(input())
    if n < 0 :
        continue
    somme +=n
print("\nSomme = ",somme)