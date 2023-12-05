from datetime import datetime
from datetime import time

date_heure_actuelle = datetime.now()
heure_actuelle = date_heure_actuelle.time()
heure_ref = time(14, 00, 00)
#vérification
print("Heure actuelle:", heure_actuelle)
print("Heure ref:", heure_ref)

if heure_actuelle > heure_ref:
    mot_accueil = "Bonsoir"
else :
    mot_accueil = "bonjour"
print(mot_accueil)

mot_saisi = print(input("Saisir mot:"))
print(mot_saisi)
#je ne connais pas encore assez python pour réussir la suite rapidement
#print("mot inversé: ", mot_inverse)

