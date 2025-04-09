import random
n = 10
L = [random.randint(1, 100) for _ in range(n)]

def tri_naif(L: list):
    compteur = 0
    for i in range(len(L) - 1, 0, -1):          # Parcourt la liste en partant de la fin vers le début
        max_index = 0
        for j in range(1, i + 1):               # Parcourt la sous-liste non triée pour trouver le maximum
            compteur += 1
            if L[j] > L[max_index]:             # Compare les éléments pour trouver le maximum
                max_index = j                   # Met à jour l'indice du maximum
        L[i], L[max_index] = L[max_index], L[i] # Permute le maximum et le dernier element de la sous liste
    return L, compteur                        

def tri_a_bulles(L: list):
    compteur = 0
    for i in range(len(L)-1):                 # Parcourt la liste de gauche à droite  
        for j in range(len(L)-1-i):           # Parcourt la sous-liste non triée i=le nb d'élément déjà triés
            compteur += 1
            if L[j] > L[j+1]:                 # Compare les éléments adjacents
                L[j], L[j+1] = L[j+1], L[j]   # Permute les éléments si nécessaire
    return L, compteur                    


print("Liste avant tri : ", L)
L.sort()
print("Liste tri : ", L)
print("Liste après tri naïf : ", tri_naif(L))
print("Liste après tri à bulles : ", tri_a_bulles(L))