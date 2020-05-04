L = []
i = 0
print("SAISIE DES VALEURS DE LA LISTE")
while True:
    L.append(input("SAISIR UNE VALEUR DE LA LISTE : "))
    while True:
        rep = input("UNE AUTRE VALEUR ? [O/N] : ")
        if rep == 'O' or rep == 'N':
            break
    i += 1
    if rep == 'N':
        break
print(L)
k = int(input("QUELLE IEME ELEMENT DE LA LISTE VOULEZ VOUS AFFICHER ? "))
if 0 < k <= len(L):
    val = L[k-1]
else:
    val = "rang invalide"
print("L =", L, ",k =", k, "->", val)