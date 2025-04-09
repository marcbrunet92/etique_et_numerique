from random import randint
N = 10
L_orig = [{0:randint(10, 1000), 1:i} for i in range(N)]
print("\nListe avant tri : ", L_orig)

def verif_ordre(L:list[dict])->bool:
    max = 0
    for i in range(len(L)):
        if L[i][0] > max:
            max = L[i][0]
        else:
            return False
    return True

def verif_stab(L:list[dict])->bool:
    if not verif_ordre(L):
        return False
    for i in range(len(L)-1):
        if L[i][0] == L[i+1][0]:
            if L[i][1] > L[i+1][1]:
                return False
    return True

def pos_max(L:list[dict])->int:
    max = 0
    for i in range(len(L)):
        if L[i][0] > L[max][0]:
            max = i
    return max

def tri_naif(L:list[dict])->list:
    compteur = 0
    for i in range(len(L) - 1, 0, -1):                      # Parcourt la liste en partant de la fin vers le début
        max_index = 0
        for j in range(1, i + 1):                           # Parcourt la sous-liste non triée pour trouver le maximum
            compteur += 1
            if L[j][0] > L[max_index][0]:                   # Compare les éléments pour trouver le maximum
                max_index = j                               # Met à jour l'indice du maximum
        L[i][0], L[max_index][0] = L[max_index][0], L[i][0] # Permute le maximum et le dernier element de la sous liste
    return L, compteur  

def tri_bulles(L:list[dict])->list:
    compteur = 0
    for i in range(len(L)-1):                               # Parcourt la liste de gauche à droite  
        for j in range(len(L)-1-i):                         # Parcourt la sous-liste non triée i=le nb d'élément déjà triés
            compteur += 1
            if L[j][0] > L[j+1][0]:                         # Compare les éléments adjacents
                L[j][0], L[j+1][0] = L[j+1][0], L[j][0]     # Permute les éléments si nécessaire
    return L, compteur

def tri_insertion(L:list[dict])->list:
    compteur = 0
    for i in range(1, len(L)):
        cle = L[i][0]
        j = i - 1
        while j >= 0 and cle < L[j][0]:
            compteur += 1
            L[j + 1][0] = L[j][0]
            j -= 1
        L[j + 1][0] = cle
    return L, compteur

def tri_rapide(L:list[dict], compteur:int=0)->list:
    if len(L) <= 1:
        return L, compteur
    pivot = randint(0, len(L)-1)
    L[-1], L[pivot] = L[pivot], L[-1]
    i = 0
    j = 0
    while i != len(L)-1:
        compteur +=1
        if L[i][0] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
            j += 1
        else:
            i += 1
        L[j], L[-1] = L[-1], L[j]
    tri_rapide(L[:j], compteur)
    tri_rapide(L[j+1:], compteur)
    return L, compteur
        
    

##################################################################################
L, compteur = tri_naif(L_orig.copy())
print("\nTri naïf\n")
print("Liste après tri naïf : ", L)
print("Compteur : ", compteur)
print("Liste triée : ", verif_ordre(L))
print("Liste stable : ", verif_stab(L))
##################################################################################
L, compteur = tri_bulles(L_orig.copy())
print("\nTri à bulles\n")
print("Liste après tri à bulles : ", L)
print("Compteur : ", compteur)
print("Liste triée : ", verif_ordre(L))
print("Liste stable : ", verif_stab(L))
##################################################################################
L, compteur = tri_insertion(L_orig.copy())
print("\nTri par insertion\n")
print("Liste après tri par insertion : ", L)
print("Compteur : ", compteur)
print("Liste triée : ", verif_ordre(L))
print("Liste stable : ", verif_stab(L))
##################################################################################
L, compteur = tri_rapide(L_orig.copy())
print("\nTri rapide\n")
print("Liste après tri rapide : ", L)
print("Compteur : ", compteur)
print("Liste triée : ", verif_ordre(L))
print("Liste stable : ", verif_stab(L))
##################################################################################