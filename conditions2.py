hour0 = input("Quelle heure est-il? ")

try:
    hour = int(hour0)
    if hour < 12:
        print("Good morning")
    elif hour < 17:
        print("Good afternoon")
    elif hour < 21:
        print("Good evening")
    else:
        print("Good night")
except ValueError:
    print("Veuillez entrer un nombre valide pour l'heure (ex: 14)")
