import math

print("=== Résolution d'une équation du second degré ===")
print("Forme générale : ax² + bx + c = 0")

# Saisie des coefficients
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

if a == 0:
    print("Ce n'est pas une équation du second degré (a ne doit pas être 0).")
else:
    # Calcul du discriminant
    delta = b**2 - 4*a*c
    print(f"Discriminant (Δ) = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"Deux solutions réelles : x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Une solution réelle double : x = {x:.2f}")
    else:
        # Cas des racines complexes
        real = -b / (2*a)
        imag = math.sqrt(-delta) / (2*a)
        print(f"Aucune solution réelle. Deux solutions complexes :")
        print(f"x1 = {real:.2f} - {imag:.2f}i")
        print(f"x2 = {real:.2f} + {imag:.2f}i")

input("Exit ...")
