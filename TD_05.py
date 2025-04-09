def exercice1(n=10):
    def u_iter(n:int):
        u = 1
        for _ in range(n):
            u = 3*u**2+4
        return u
    def u_rec(n:int):
        if n ==0:
            return 1
        return 3*u_rec(n-1)**2+4
    print(u_iter(n), "itératif")
    print(u_rec(n), "récursif")

def exercice2(n=10):
    def s_iter(n:int):
        s = 0
        for i in range(1, n+1):
            s += i**-3
        return s
    def s_rec(n:int):
        if n == 1:
            return 1
        return n**-3 + s_rec(n-1)
    print(s_iter(n), "itératif")
    print(s_rec(n), "récursif")

def exercice3(n=2):
    a = n
    def r_iter(n, a):
        r = a/2
        for _ in range(n):
            r = (r + (a/r))/2
        return r
    def r_rec(n, a):
        if n == 0:
            return a/2
        return (r_rec(n-1, a) + (a/r_rec(n-1, a)))/2
    print(r_iter(n, a), "itératif")
    print(r_rec(n, a), "récursif")
    print("vrai racine : ", a**0.5)

def exercice4(n=100):
    from random import randint
    L = [randint(1,1000) for _ in range(n)]
    def max_iter(L:list):
        maximum = 1
        for i in range(len(L)):
            if L[i] > maximum:
                maximum = L[i]
        return maximum
    def max_rec(L:list):
        if len(L) == 1:
            return L[0]
        temp = max_rec(L[1:])
        if L[0] > temp:
            return L[0]
        return temp
    print(max_iter(L), "itératif")
    print(max_rec(L), "récursif")
    print("vrai max = ", max(L))
    del randint

def exercice5(n=10):
    def f_iter(n):
        f = [0, 1]
        if n in [0, 1]:
            return n
        for _ in range(2, n + 1):
            f.append(f[-1] + f[-2])
        return f[-1]
    def f_rec(n):
        if n in [0, 1]:
            return n
        return f_rec(n-2)+f_rec(n-1)
    print(f_iter(n), "itératif")
    print(f_rec(n), "récursif")

def exercice6():
    with open('touslesmots.txt','r',encoding='utf-8') as f:
        table=f.read().split(' ')
    if not table:
        return "liste vide"
    from random import randint
    mot_cible = table[randint(0, len(table)-1)]
    def recherche0(mot_cible: str, L: list) -> tuple[int, str, int]:
        compteur = 0
        for i in range(len(L)):
            compteur +=1
            if L[i] == mot_cible:
                return i, L[i], compteur
        return -1, -1, compteur
    def recherche_dicho(mot_cible:str, L:list)->tuple[int, str, int]:
        m =0
        M = len(L)
        compteur = 0
        while m <= M:
            compteur += 1
            mil = (M+m)//2
            if mot_cible == L[mil]:
                return mil, L[mil], compteur
            elif mot_cible < L[mil]:
                M = mil-1
            elif mot_cible > L[mil]:
                m = mil+1
        return -1, -1, compteur
    def dicho_rec(mot_cible, L, m, M, compteur=0):
        if m > M:
            return -1, compteur
        mil = (m + M) // 2
        compteur += 1
        if L[mil] == mot_cible:
            return mil, L[mil], compteur
        elif mot_cible < L[mil]:
            return dicho_rec(mot_cible, L, m, mil - 1, compteur)
        else:
            return dicho_rec(mot_cible, L, mil + 1, M, compteur)
    print("trouvé (recherche0) : ",recherche0(mot_cible, table))
    print("trouvé (recherche_dicho) : ",recherche_dicho(mot_cible, table))
    print("trouvé (dicho_rec) : ", dicho_rec(mot_cible, table, 0, len(table)-1))
    print("cherché : ", mot_cible)
    del randint

def exercice7(a=2, b=5):
    def pgcd(a, b):
        if b==0:
            return a
        else :
            return pgcd(b, a % b)
    print(pgcd(a, b))

def exercice8(n=10):
    def base2(n: int) -> str:
        if n == 0:
            return "0"
        elif n == 1:
            return "1"
        else:
            return base2(n // 2) + str(n % 2)
    print(f"conversion de {n} : {base2(n)}")

def exercice9(s="abcd"):
    def inversion_rec(s: str) -> str:
        if s == "":
            return ""
        if len(s) == 1:
            return s
        return inversion_rec(s[1:]) + s[0]
    print(inversion_rec(s))

def exercice10(x=2, n=10):
    def expo_naif_rec(x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else :
            return x * expo_naif_rec(x, n-1)
    def expo_rapide_rec(x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            mil = expo_rapide_rec(x * x, n // 2)
            return mil
        else:
            mil = expo_rapide_rec(x * x, (n - 1) // 2)
            return x * mil
    print(expo_naif_rec(x, n))
    print(expo_rapide_rec(x, n))

def exercice11(n=3):
    def hanoi(n, d:int=1, f:int=3, m:int=2)->None:
        if n == 1:
            print(f"Déplacer le disque {n} de la tour {d} vers la tour {f}")
        else:
            hanoi(n-1, d, m, f)
            print(f"Déplacer le disque {n} de la tour {d} vers la tour {f}")
            hanoi(n-1, m, f, d)
    hanoi(n)

def exercice12(n=10):
    import random
    L = [random.randint(1, 100) for _ in range(n)]
    def parite_recursive(L:list)->list[list[int],list[int]]:
        if len(L) == 0:
            return [], []
        else:
            pair, impair = parite_recursive(L[1:])
            if L[0] % 2 == 0:
                pair.append(L[0])
            else:
                impair.append(L[0])
            return pair, impair
    def parite_iterative(L:list)->list[list[int],list[int]]:
        pair = []
        impair = []
        for i in L:
            if i % 2 == 0:
                pair.append(i)
            else:
                impair.append(i)
        return pair, impair
    print(parite_recursive(L))
    print(parite_iterative(L))
    del random

for i in range(1, 13):
    print(f"Exercice {i} :")
    eval(f"exercice{i}()")