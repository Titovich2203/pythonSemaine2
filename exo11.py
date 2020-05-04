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
L[0], L[len(L)-1] = L[len(L)-1], L[0]
print("APRES ECHANGE ON A : ")
print(L)