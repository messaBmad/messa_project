import requests

# Ajouter un utilisateur
nouveau = {"nom": "Yassine", "âge": 22}
r = requests.post("http://127.0.0.1:5000/api/utilisateurs", json=nouveau)
print(r.json())

# Obtenir tous les utilisateurs
r = requests.get("http://127.0.0.1:5000/api/utilisateurs")
print(r.json())
