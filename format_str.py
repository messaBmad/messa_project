def formater(nom , prenom):
    NOM = nom.upper()
    Prenom = prenom.capitalize()
    np = f"{NOM} {Prenom}"
    return np
    #return NOM , Prenom

n = input("Votre nom: ")
p = input("Votre prénom: ")
print(f"Bonjour M. {formater(n,p)}")

print()
input("Exit ...")
