from matplotlib import pyplot as plt

def eratosthene(N: int):
    nombres = [i for i in range(0, N + 1)]
    premiers = []
    for i in range(2, N + 1):
        if nombres[i] != 0:
            premiers.append(i)
            k = 2
            while k * i <= N:
                nombres[k * i] = 0
                k += 1
    return premiers

def goldbach_v1(n:int)->tuple:
    premiers=eratosthene(n)
    entiers_pairs=[i for i in range(0, n+1, 2)]
    compte=[0]*len(entiers_pairs)
    for i in range(len(entiers_pairs)):
        x=entiers_pairs[i]
        j1=0
        while premiers[j1]<=x//2:
            j2=j1 #car p2>=p1
            while j2<len(premiers) and premiers[j2]+premiers[j1]<=x:
                if premiers[j2]+premiers[j1]==x:
                    compte[(x//2)-2]+=1
                j2+=1
            j1+=1
    return entiers_pairs,compte

def marc(n:int)->tuple:
    premiers=eratosthene(n)
    entiers_pairs=[i for i in range(4, n+1, 2)]
    compte_dictionnaire= {}
    for x in entiers_pairs:          #x est le nombre pour lequel on cherche les p1 et p2
        compte_dictionnaire[x] = 0   #On cree un dictionnaire pour mettre le nb de fois que x peut s'écrire p1+p2
        for p1 in premiers:          #p1 parcourt les premiers
            for p2 in premiers:      #p2 parcourt les premiers
                if p1>p2:
                    continue         #On teste tant que p2>=p1
                if p1+p2 == x:
                    compte_dictionnaire[x]+=1
    compte = []                      # On parcourt le dictionnaire
    for cle, valeur in compte_dictionnaire.items():
        compte.append(valeur)
    return entiers_pairs,compte

def goldbach_v2(n=10**5):
    premiers = eratosthene(n)
    entiers_pairs = [i for i in range(4, n + 1, 2)]
    compte = [0]*(len(entiers_pairs)+2)
    for x in entiers_pairs:  # x est le nombre pour lequel on cherche les p1 et p2
        for p1 in premiers:  # p1 parcourt les premiers
            for p2 in premiers:  # p2 parcourt les premiers
                if p1 > p2:
                    continue  # On teste tant que p2>=p1
                if p1 + p2 == x:
                    compte[x//2] += 1
    del(compte[1:3])
    return entiers_pairs, compte

fin = 10**4
# Créer la fenêtre avec 3 sous-graphiques (1 colonne, 3 lignes)
plt.figure(figsize=(10, 10))

# Premier graphique - Goldbach v1
plt.subplot(3, 1, 1)
liste_x, liste_y = goldbach_v1(fin)
plt.plot(liste_x, liste_y, '.')
plt.title("Goldbach v1")

# Deuxième graphique - Goldbach v2
plt.subplot(3, 1, 2)
liste_x, liste_y = marc(fin)
plt.plot(liste_x, liste_y, '.')
plt.title("Goldbach v2--la mienne")

# Troisième graphique - Goldbach v3
plt.subplot(3, 1, 3)
liste_x, liste_y = goldbach_v2(fin)
plt.plot(liste_x, liste_y, '.')
plt.title("Goldbach v2")

# Afficher tous les graphiques dans la même fenêtre
plt.tight_layout()  # Ajuste l'espacement entre les graphiques
plt.show()









"""
def eratosthene(N: int) -> list:
    nombres = [i for i in range(N + 1)]
    premiers = []

    for i in range(2, N + 1):
        if nombres[i] != 0:
            premiers.append(i)
            k = 2
            while i * k <= N:
                nombres[i * k] = 0
                k += 1

    return premiers

def goldbach_v1(N: int) -> tuple:
    premiers = eratosthene(N)
    entiers_pairs = [i for i in range(4, N + 1, 2)]
    compte = [0] * len(entiers_pairs)

    for i in range(len(entiers_pairs)):
        x = entiers_pairs[i]
        j1 = 0
        while j1 < len(premiers) and premiers[j1] <= x // 2:
            j2 = j1
            while j2 < len(premiers) and premiers[j1] + premiers[j2] <= x:
                if premiers[j1] + premiers[j2] == x:
                    compte[i] += 1
                j2 += 1
            j1 += 1
    return entiers_pairs, compte

def goldbach_v2(N: int) -> tuple:
    premiers = eratosthene(N)
    entiers_pairs = [i for i in range(4, N + 1, 2)]
    compte = [0] * len(entiers_pairs)

    compte[0] = 1
    j1 = 1

    while j1 < len(premiers) and premiers[j1] <= N // 2:
        p1 = premiers[j1]
        j2 = j1

        while j2 < len(premiers) and p1 + premiers[j2] <= N:
            p2 = premiers[j2]
            pos = (p1 + p2) // 2 - 2
            compte[pos] += 1
            j2 += 1

        j1 += 1

    return entiers_pairs, compte

print(eratosthene(100))
print(goldbach_v1(30))
import matplotlib.pyplot as plt
liste_x, liste_y = goldbach_v2(10**4)
plt.plot(liste_x, liste_y, '.')
plt.show()

"""