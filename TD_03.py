#Ex 1
def f1(x:float)->float:
    return x**2+4*x+2

#Ex 2
def f2(x):
    x**2+1

#Ex 3
def f3(x):
    print(x**2+1)

#Ex 4
def p17(x:int)->int:
    return x**17

#Ex 5
from math import sqrt

def racine_carree(x:float)->float:
    if int(x)==float(x): #Ou round(x)
        y = 0
        while y**2 != x:
            y +=1
            if y**2>x:
                return sqrt(x)
        return y
    else:
        return sqrt(x)

#Ex 6
def somme_carres(n:int)->int:
    resultat = 0
    for x in range(1,n+1):
        resultat += 1/x**2
    return resultat

#Ex 7
def puissance(x:float, y:float)->float:
    return x**y

#Ex 8
def quatres(n:int)->int:
    return puissance(4, n)

#Ex 9
def nieme(t:str, n:int)->str:
    if n<len(t):
        return t[n]
    return t[-1]

#Ex 11
def CarreCube(x:float)->float:
    return x**2
    return x**3 #Ne sera pas retourné la fonction s'arrete au premier return

#Ex 11.1
def CarreCube(x:float)->float:
    return (x**2,x**3)

#Nb premier
def premiers(N:int):
    ensemble_a_tester = list(range(0, N+1))
    resultat = ensemble_a_tester.copy()
    for i in ensemble_a_tester:
        for j in range(1, len(ensemble_a_tester)):
            print(i, ensemble_a_tester)
            if ensemble_a_tester[i]%j ==0:
                print('a')
                del(resultat[i])
                print(resultat)
                break
    print(resultat)

print(premiers(100))