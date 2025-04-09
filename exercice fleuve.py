#Ex 45 = le crible d'ératosthène



def ex12(n, p):
    if n%p!=0:
        return n//p
    return 0

def ex13(annee):
    if (annee%4 == 0 and annee%100 != 0 ) or annee%400 == 0:
        return 29
    return 28

def ex14(a, b):
    if a>=b:
        return b, a
    return a, b

def ex15(l):
    if len(l)==0:
        return [], []
    elif len(l)==1:
        return l, []
    else :
        return l[0:len(l) // 2], l[(len(l) // 2):-1]

def ex16(j, m):
    signe_astrologique = ["le Capricorne", "le Verseau", "les Poissons", "le Bélier", "le Taureau", "les Gémeaux", "le Cancer", "le Lion", "la Vierge", "la Balance", "le Scorpion", "le Sagittaire"]
    if j>21:
        return signe_astrologique[m]
    else :
        return signe_astrologique[m-1]

def ex17_1(j, m, a):
    mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m>12 or m<1 or j<1 or a<1:
        return False
    else:
        if (a%4 == 0 and a%100 != 0 ) or a%400 == 0:
            mois[1] = 29
        if j>mois[m-1]:
            return False
    return True

def ex18_1(p, n):
    a = [p]
    q = 1
    while a[-1]<n:
        q +=1
        a.append(p*q)
    a.pop()
    return a

def ex18_2(p, n):
    a = []
    for x in range(1, n):
        a.append(x*p)
        if a[-1]>n:
            a.pop()
            break
    return a

def ex19(M):
    b = 1
    while 1==1:
        if b**3>M:
            return b-1
        b+=1

def ex20(n, m):
    p = 0
    while 1==1:
        if n**p>m:
            return p-1
        p+=1

def ex30_1(s):
    fin = ""
    for i in range(len(s)):
        fin += s[-i-1]
    return fin

def ex34(l, p):
    resultat = 0
    for i in range(max(l)):
        if i*p in l:
            resultat += 1
    return resultat

def ex35(L, n):
    resultat = []
    for i in range(len(L)):
        if L[i] == n:
            resultat.append(i)
    return resultat

def ex45_1(N):
    L = [i for i in range(N)]
    Lp = [1]
    for i in range(2, N):
        if L[i] != 0:
            Lp.append(i)
        k = 1
        while i*k < N:
            L[i*k] = 0
            k += 1
    return Lp, L

def ex45_2(n):
    if n == 1:
        return True
    if ex45_1(n)[1][-1] == 0:
        return False
    return True

def ex50(n=1000000):
    L_n = [i for i in range(4, n+1, 2)]
    termes = [0]*(len(L_n))
    p_1_liste = ex45_1(n)[0] #Liste des premiers jusqu'à n
    for j in range(len(L_n)):
        for i in range(len(p_1_liste)):
            if L_n[j]-p_1_liste[i] <0:
                break
            #print(i, j)
            #print(L_n[j]-p_1_liste[i])
            if ex45_2(L_n[j]-p_1_liste[i]):
                termes[j] = (p_1_liste[i], L_n[j]-p_1_liste[i])
    return len(L_n), len(termes), len(p_1_liste)
print(ex45_2(1000))