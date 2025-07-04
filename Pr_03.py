"""
    L_objets =[(4,2,0) ,(3,3,1) ,(2,5,2)]
    L_objets[k][0] : poids
    L_objets[k][1] : valeur
    L_objets[k][2] : index
"""

def valeur_choix(L_e:list[int],L_objets:list[tuple[int]])->int:
    """
    Calcule la valeur totale des objets choisis
    :param L_e: liste d'index d'objets choisis
    :param L_objets: liste d'objets
    :return: valeur totale
    """
    return sum(L_objets[k][1] for k in L_e)

def poids_choix(L_e:list[int],L_objets:list[tuple[int]])->int:
    """
    Calcule le poids total des objets choisis
    :param L_e: liste d'index d'objets choisis
    :param L_objets: liste d'objets
    :return: poids total
    """
    return sum(L_objets[k][0] for k in L_e)

def ratio(o:tuple[int])->float:
    """
    Calcule le ratio valeur/poids d'un objet
    :param o: objet
    :return: ratio
    """
    return o[1]/o[0] if o[0] != 0 else 0

def tri(L_objets:list[tuple[int]])->list:
    """
    Trie la liste d'objets par ordre décroissant de ratio valeur/poids
    :param L_objets: liste d'objets
    :return: liste d'objets triée
    """
    def tri_insertion_decroissant(L: list[tuple[int]]) -> None:
        """
        Trie la liste L par ordre décroissant de ratio valeur/poids en utilisant le tri par insertion.
        :param L: liste d'objets
        """
        for i in range(1, len(L)):
            key = L[i]
            j = i - 1
            while j >= 0 and ratio(L[j]) < ratio(key):
                L[j + 1] = L[j]
                j -= 1
            L[j + 1] = key
    def tri_rapide(L:list[tuple[int]]) -> list:
        """
        Trie la liste d'objets par ordre décroissant de ratio valeur/poids
        en utilisant l'algorithme de tri rapide.
        :param L: liste d'objets
        :return: liste d'objets triée
        """
        if len(L) <= 1:
            return L
        else:
            pivot = L[0]
            pivot_ratio = ratio(pivot)
            # Partitionner les objets en fonction du ratio
            gauche = [obj for obj in L[1:] if ratio(obj) >= pivot_ratio]
            droite = [obj for obj in L[1:] if ratio(obj) < pivot_ratio]
            # Combiner les résultats triés
            return tri(gauche) + [pivot] + tri(droite)
    L_triee = L_objets.copy()
    tri_insertion_decroissant(L_triee) # ou tri_rapide(L_triee)
    return L_triee

def  SaD_glouton(L_objets:list[tuple[int]],P:int)->tuple[list[int], int, int]:
    """
    Algorithme glouton pour le problème du sac à dos
    :param L_objets: liste d'objets
    :param P: poids maximum
    :return: liste d'index d'objets choisis, valeur totale, poids total
    """
    L_triee = tri(L_objets)
    L_e = []
    while True:
        if len(L_triee) == 0:
            break
        o = L_triee[0]
        if poids_choix(L_e + [o[2]],L_objets) <= P:
            L_e.append(o[2])
            L_triee.remove(o)
        else:
            break
    return L_e, valeur_choix(L_e,L_objets), poids_choix(L_e,L_objets)

def SaD_pDyn(L_objets:list[tuple[int]],P:int)->tuple[list[int],int ,int]:
    """
    Algorithme dynamique pour le problème du sac à dos
    :param L_objets: liste d'objets
    :param P: poids maximum
    :return: liste d'index d'objets choisis, valeur totale, poids total
    """
    #initialisation
    import numpy as np
    nl = len(L_objets)
    nc = P + 1
    V=np.zeros ((nl, nc) ,np.uint64)
    for i in range(len(V)):
        o=L_objets[i]
        for j in range(len(V[i])):
            if i==0: #cas de base
                if j>=o[0]:
                    V[i,j]=o[1]
            else:
                if o[0] > j or V[i-1,j] > V[i-1,j - o[0]] + o[1]:
                    V[i,j]=V[i-1,j]
                else:
                    V[i,j]=V[i-1,j - o[0]] + o[1]    
    #reconstruction de la solution:
    L_e =[]
    j=P
    for i in range(len(V) -1,-1,-1):
        if i>0:
            if V[i,j] != V[i-1,j]:#on a pris l’objet i
                L_e.append(i)
                j -= L_objets[i][0]
        else:
            if  V[i,j] != 0: #on a pris l’objet 0
                L_e.append(i)
    return L_e ,valeur_choix(L_e ,L_objets),poids_choix(L_e ,L_objets)

if __name__ == "__main__":
    from random import randint, random #import des fonctions de randomisation
    import time #import de la fonction time pour le chronométrage
    N=100 #nombre d’objets
    L_objets2 =[] #liste d’objets
    somme_p =0 #somme des poids
    for i in range(N): #on crée N objets
        r=random()*0.2+5 #on contraint les objets a avoir un ration v/p similaire (entre 5 et 5.2 ici)
        p=randint(100 ,1000) #les poids sont variables
        v=int(r*p) #la valeur est proportionnelle au poids
        L_objets2.append ((p,v,i)) #on ajoute l’objet `a la liste
        somme_p +=p #on calcule la somme des poids
    P=somme_p //3 #on se limite `a un tiers du poids total , ce qui enl`eve les cas triviaux et oblige `a faire des bons choix.
    print(f"poids max : {P}") #affichage du poids maximum
    # Chronométrer la fonction gloutonne
    start_time = time.time()
    result_glouton = SaD_glouton(L_objets2, P)
    end_time = time.time()
    print("Temps d'exécution (glouton):", end_time - start_time, "secondes")
    print(result_glouton)

    # Chronométrer la fonction dynamique
    start_time = time.time()
    result_pDyn = SaD_pDyn(L_objets2, P)
    end_time = time.time()
    print("Temps d'exécution (dynamique):", end_time - start_time, "secondes")
    print(result_pDyn)