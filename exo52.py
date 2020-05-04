while True:
    m = input("VOTRE MOT DE PASSE : ")
    sur = True
    if len(m) < 8:
        sur = False
    else:
        cpt = 0
        for c in m:
            if 'a' <= c <= 'z':
                cpt += 1
        if cpt == 0:
            sur = False
        else:
            cpt = 0
            for c in m:
                if 'A' <= c <= 'Z':
                    cpt += 1
            if cpt == 0:
                sur = False
            else:
                cpt = 0
                for c in m:
                    try:
                        if 0 <= int(c) <= 9:
                            cpt += 1
                    except:
                        cpt = cpt
                if cpt == 0:
                    sur = False
                else:
                    cpt = 0
                    for c in m:
                        if c in ['-','!','?',',','.',';',':','*','~']:
                            cpt += 1
                    if cpt == 0:
                        sur = False
                    else:
                        sur = True
    if sur == True:
        print("le mot de passe :",m,"est sur !!!")
        break
    else:
        print("le mot de passe :", m, "n'est pas sur !!!")