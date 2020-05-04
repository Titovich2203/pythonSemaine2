while True:
    verbe = input("VERBE DU PREMIER GROUPE : ")
    if verbe[len(verbe)-2: ] == "er":
        break
verbe = verbe[:len(verbe)-2]
print()
print("CONJUGAISON AU PRESENT DE l'INDICATIF")
print("=====================================")
print("Je",(verbe+"e"))
print("Tu",(verbe+"es"))
print("Il/elle",(verbe+"e"))
print("Nous",(verbe+"ons"))
print("Vous",(verbe+"ez"))
print("Ils/elles",(verbe+"ent"))