def calcul_mantisse(x:float)->list :
    representation = []
    for _ in range(0, 23):
        x *= 2
        if x >= 1:
            representation.append(1)
            x += -1
        else:
            representation.append(0)
    return representation

def verif_mantisse(l:list)->float:
    resultat = 0
    for i in range(0, 23):
        resultat += l[i]/(2**(1+i))
    return resultat

#a doit contenir des flottants entre [0, 1[
essais = [0.3, 0.625]
for essai in essais:
    print(calcul_mantisse(essai))
    print(verif_mantisse(calcul_mantisse(essai)))