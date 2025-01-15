nom_classe = input("Donner le nom de la classe : ")
nombre_etudiant = int(input("Donner le nombre total des étudiants : "))

note_max = 0
note_min = 20
somme_notes = 0 
nombre_totale_notes = 0

for n in range(1, nombre_etudiant + 1):
    print(f"\nÉtudiant {n} :")
    for i in range(1, 5):
        note = -1
        while note < 0 or note > 20:
            note = float(input(f"Donner la note {i} de l'étudiant {n} (entre 0 et 20) : "))
            if note < 0 or note > 20:
                print("Erreur : La note doit être entre 0 et 20. Réessayez.")
        if note > note_max:
            note_max = note
        if note < note_min:
            note_min = note
        somme_notes += note
        nombre_totale_notes += 1
print(f"\nFin de la saisie pour la classe {nom_classe}.")
print(f"Note maximale de la classe : {note_max}")
print(f"Note minimale de la classe : {note_min}")
print(f"La somme des notes de la classe : {somme_notes}")