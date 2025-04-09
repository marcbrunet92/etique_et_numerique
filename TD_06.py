from random import randint
N = 10
L_orig = [{0:randint(10, 1000), 1:i} for i in range(N)]
L = L_orig.copy() # pareil que L = [L_orig[i] for i in range(len(L_orig))]

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
    