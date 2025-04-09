global mois
def ex6_2():
    jours = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    jour_d_aujourd_hui = 3
    u = []
    for i in range(jour_d_aujourd_hui, 41+jour_d_aujourd_hui):
        u.append(jours[i%7])
    print(u)
def ex7_1():
    jour_du_mois = 2
    u = []
    for i in range(jour_du_mois, 181+jour_du_mois):
        u.append(i%30)
    print(u)

def ex7_2():
    mois=[31, 28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
    mois_actuel = 3
    u = []
    for i in range(mois_actuel, 4+mois_actuel):
        for j in range(1, mois[i%7]+1):
            u.append(j)
    print(u)

def ex12_1(annee):
    if (annee%4 == 0 and annee%100 != 0 ) or annee%400 == 0:
        return True
    return False

def ex12_3(annee):
    mois=[31, int(ex12_1(annee))+28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
    return mois

def ex12_4(annee, mois_de_depart):
    mois = ex12_3(annee)
    u = []
    for i in range(mois_de_depart, 4+mois_de_depart):
        for j in range(1, mois[i%7]+1):
            u.append(j)
    return u

def ex19():
    import random
    cartes=[25, 50, 75, 100, 200]
    d = 0
    n = 0
    cartesj = []
    while d<1000:
        c = random.choice(cartes)
        n += 1
        if c+d <= 1000:
            d+=c
            cartesj.append(c)
    return n

def statsmilleborne(en_combien):
    import numpy as np
    a = []
    b = 0
    for _ in range(en_combien):
        a.append(ex19())
    b = np.mean(a)
    print('le nb de tours moyen est', b)

def pierre(année, jours, mois_actuel):
    mois = ex12_3(année)
    j = jours
    x = mois_actuel #x = mois
    for i in range (10000) :
        print (str(j)+"/"+str(x)+"/"+str(année))
        j += 1
        if j == mois[x] + 1 :
            j = 1
            x += 1
            if x == 12 :
                x = 1
                année += 1
                if (année % 400 == 0) or (a% 4 ==0 and a % 100 != 0) :
                    mois[1] = 29
                else :
                    mois[1] = 28


def ex20(fin):
    l_v = []
    j = 3
    d = 9
    m = 10
    a = 2024
    mois=[31,29,31,30,31,30,31,31,30,31,30,31]
    jours = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    while len(l_v)<=fin:
        pass
