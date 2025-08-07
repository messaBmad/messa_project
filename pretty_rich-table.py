from rich.table import Table
from rich.console import Console

# Créer la console
console = Console()

# Créer la table
table = Table(title="Ma Table")

# Définir les colonnes
table.add_column("Colonne 1", style="cyan", no_wrap=True)
table.add_column("Colonne 2", style="magenta")
table.add_column("Colonne 3", style="green")

# Ajouter les lignes
table.add_row("Ligne 1, Col 1", "Ligne 1, Col 2", "Ligne 1, Col 3")
table.add_row("Ligne 2, Col 1", "Ligne 2, Col 2", "Ligne 2, Col 3")
table.add_row("Ligne 3, Col 1", "Ligne 3, Col 2", "Ligne 3, Col 3")

# Afficher la table
console.print(table)

print()

from prettytable import PrettyTable

# Créer la table
table = PrettyTable()

# Définir les colonnes
table.field_names = ["Colonne 1", "Colonne 2", "Colonne 3"]

# Ajouter les lignes
table.add_row(["Ligne 1, Col 1", "Ligne 1, Col 2", "Ligne 1, Col 3"])
table.add_row(["Ligne 2, Col 1", "Ligne 2, Col 2", "Ligne 2, Col 3"])
table.add_row(["Ligne 3, Col 1", "Ligne 3, Col 2", "Ligne 3, Col 3"])

# Afficher la table
print(table)

print()
input("Press any key to continue ...")