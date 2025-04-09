def est_bissextile(annee):
    if (annee%4 == 0 and annee%100 != 0 ) or annee%400 == 0:
        return True
    return False

def definirMois(annee):
    mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if est_bissextile(annee):  # Ajustement pour les années bissextiles
        mois[1] = 29
    return mois

def jour_semaine(jour, mois, annee):
    jour_reference = 1
    mois_reference = 1
    annee_reference = 2023
    jour_semaine_reference = 0
    total_jours = 0       # cette fonction calcule le total de jour entre la date et la date de reference pour faire modulo 7
    for an in range(annee_reference, annee):
        total_jours += 366 if est_bissextile(an) else 365   #ajoute le nb de jours en fonction des années
    nb_jours_par_mois = definirMois(annee)                  #ajoute le nb de jour du debut de l'année cible jusqu'au mois de l'année cible 
    for m in range(1, mois):
        total_jours += nb_jours_par_mois[m - 1]
    total_jours += jour - jour_reference
    return (jour_semaine_reference + total_jours) % 7       #return 0 pour dimanche, 5 pour vendredi.

def vendredi13(combien_de_vendredi=100): #par defaut la liste des 100 prochains vendredi
    """
    import time
    date = time.localtime()
    d = date.tm_mday        # Jour du mois
    m = date.tm_mon         # Mois de l'année (1 = janvier, ..., 12 = décembre)
    a = date.tm_year
    """
    d = 9
    m = 10
    a = 2024
    
    l_v = []
    mois = definirMois(a)
    while len(l_v)<=combien_de_vendredi:
        if jour_semaine(d, m, a) == 5 and d == 13:
            l_v.append(str(d)+"/"+str(m)+"/"+str(a))
            print(str(d)+"/"+str(m)+"/"+str(a))
        d += 1
        if d > mois[m-1]:
            d = 1
            m+=1
        if m > 12:
            a+=1
            mois = definirMois(a)
            m=1
            
if __name__ == "__main__":
    vendredi13()
input("Appuyez sur entrée pour finir le programme")
