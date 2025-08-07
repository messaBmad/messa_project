from datetime import datetime
from dateutil.relativedelta import relativedelta

# Demander à l'utilisateur de saisir deux dates
date1_str = input("Entrez la première date (format AAAA-MM-JJ) : ")
date2_str = input("Entrez la deuxième date (format AAAA-MM-JJ) : ")

# Convertir les chaînes en objets datetime
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# Calculer la différence avec relativedelta
if date1 > date2:
    date1, date2 = date2, date1  # s'assurer que date1 <= date2

diff = relativedelta(date2, date1)

# Afficher le résultat
print(f"Période entre les deux dates : {diff.years} années, {diff.months} mois, {diff.days} jours")
