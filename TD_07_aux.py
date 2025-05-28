print("Ceci est le fichier classes développée par R. Bel")
print("Version 1.001 du 21-05-25")
print("Définitions dans ce fichier :")
print("-classe pile")
print("-fonction pile_vide")
print("-classes file, filep (file de priorité) et filep_unique (file de priorité avec mise à jour de la priorité")
print("-fonctions file_vide, filep_vide et filepu_vide")
print("-fonction genere_file_aleatoire")
print("- classe graphe_base")
print("- classes graphe, graphe_p, graphe_o et graphe_op, sous-classes de graphe" )
print("- fonctions genere_graphe_aleatoire et genere_graphe_p_aleatoire")
print("- fonctions graphe_from_liste et graphe_p_from_liste")
print("Ce fichier importe également numpy aliasé en np, et les fonctions random et randint du module random")

print("")
print("")

print("Taper help(pile), help(file) ou help(graphe) pour avoir de l'aide sur ces diverses classes")

class pile:
    """Ceci est la classe pile
    Une pile est une structure de données de type LIFO (Last In First Out)
    On peut y insérer des éléments, les dépiler (enlever le dernier élément) et en afficher le contenu.
    On peut aussi tester si la pile est vide, et afficher le sommet de la pile sans le dépiler.
    """
    def __init__(self):
        """Constructeur de la classe pile"""        
        self.data=[]


    def __repr__(self):
        """Retourne une représentation de la pile sous forme de chaîne de caractères
        """
        return "\n"+self.chaine_pile()




    def est_vide(self):
        """teste si la pile est vide
        Utilisation : si P est une pile, on tape P.est_vide()
        """
        if len(self.data)==0:
            return True
        return False

    def pop(self):
        """enlève le dernier élément de la pile (LIFO) et le retourne.
        Lève une exception si la pile est vide
        Utilisation : si P est une pile, on tape P.pop()
        """
        try :
            assert not self.est_vide()
        except:
            raise Exception("La pile est vide")

        return self.data.pop()

    def depile(self):
        """Alias de pop"""
        return self.pop()

    def empile(self,element):
        """Alias de insert"""
        self.insert(element)

    def insere(self,element):
        """Alias de insert"""
        self.insert(element)

    def push(self,element):
        """Alias de insert"""
        self.insert(element)


    def insert(self,element):
        """Ajoute un élément en haut de la pile
        Utilisation : si P est une pile et e un élément, on tape P.insert(e)"""
        self.data.append(element)

    def top(self):
        """Retourne le haut de la pile (priorité LIFO) sans modifier la pile
        Utilisation : si P est une pile, on tape P.top()"""
        a=self.pop()
        self.empile(a)
        return a

    def affiche_pile(self):
        print('\n'+self.chaine_pile())

    def chaine_pile(self):
        if self.est_vide():
            return "----"
        a=self.pop()
        retour=str(a)+"\n"+self.chaine_pile()
        self.empile(a)
        return retour


def pile_vide():
    return pile()

def genere_pile_aleatoire(n,distinct=False):
    from random import randint
    pile=pile_vide()
    n=min(26,n)
    p=0
    l=[]
    while p<n:
        p+=1
        goOn=True
        while goOn:
            a=randint(65,90)
            if not distinct or chr(a) not in l:
                l.append(chr(a))
                goOn=False
    for e in l:
        pile.empile(e)
    return pile







import heapq as hpq


class file:
    """Ceci est la classe file, implémentée à l'aide de la classe hpq du module heapq. On considère une file simple comme une file de priorité où tous els éléments ont une priorité à pmax+1"""
    def __init__(self):
        self.data=[]

    def __repr__(self):
        return self.chaine_file()

    def get_max_p(self):
        if self.est_vide():
            return 0
        else:
            max=0
            for e in self.data:
                if e[0]>max:
                    max=e[0]
            return max

    def est_vide(self):
        """Retourne True si la file est vide, False sinon
        Utilisation : si F est une file, on tape F.est_vide()"""
        return len(self.data)==0

    def insere(self,e):
        """Ajoute un élément dans la file
         Utilisation : si F est une file et e un élément, on tape F.insere(e)"""
        hpq.heappush(self.data,(self.get_max_p()+1,e))

    def insert(self,e):
        """alias de insere"""
        self.insere(e)

    def enfile(self,e):
        """alias de insere"""
        self.insere(e)

    def retire(self):
        """Retire un élément selon la priorité FIFO et en retourne la valeur
        Lève une exception si la pile est vide
        Utilisation : si F est une file, on tape F.retire()"""
        try:
            p,a=hpq.heappop(self.data)
        except:
            raise Exception("La file est vide")
        return a

    def affiche_file(self):
        print(self.chaine_file)

    def top(self):
        return self.data[0][1]

    def chaine_file(self):
        file_aux=file()
        s=''
        while not self.est_vide():
            c_e=self.retire()
            s=str(c_e)+'->'+s
            file_aux.enfile(c_e)

        while not file_aux.est_vide():
            c_e=file_aux.retire()
            self.enfile(c_e)
        return s



class filep:
    """Ceci est la classe filep, implémentée à l'aide de la classe hpq du module heapq
    Afin de conserver un comportement FIFO en cas d'égalité des priorités, les éléments en interne sont de la forme (p,pp,e) où p est la priorité, pp une priorité incrémentielle en cas d'insertion avec égalité de p, et e l'élément"""
    def __init__(self):
        self.data=[]

    def __repr__(self):
        return self.chaine_file()

    def est_vide(self):
        """Retourne True si la file est vide, False sinon"""
        return len(self.data)==0

    def get_max_pp(self,p):
        pp_max=-1
        for e in self.data:
            if e[0]==p and e[1]>pp_max:
                pp_max=e[1]
        return pp_max

    def insere(self,e,p):
        """Ajoute un élément dans la file"""
        try:
            assert type(p)==int
            assert p>=0
        except:
            raise Exception('Format de données incorrect')
        pp=self.get_max_pp(p)+1
        hpq.heappush(self.data,(p,pp,e))

    def enfile(self,e,p):
        """alias de insere"""
        self.insere(e,p)

    def insert(self,e,p):
        """alias de insere"""
        self.insere(e,p)

    def retire(self):
        """Retire un élément selon la priorité FIFO"""
        try:
            p,pp,a=hpq.heappop(self.data)
        except:
            raise Exception("La file est vide")
        return a,p

    def pop(self):
        """alias de retire"""
        return self.retire()

    def top(self):
        return self.data[0][2],self.data[0][0]

    def chaine_file(self):
        file_aux=filep()
        s=''
        while not self.est_vide():
            c_e=self.retire()
            s=str(c_e)+'->'+s
            file_aux.enfile(c_e[0],c_e[1])

        while not file_aux.est_vide():
            c_e=file_aux.retire()
            self.enfile(c_e[0],c_e[1])
        return s

    def affiche_file(self):
        print(self.chaine_file)



class filep_unique:
    """Ceci est la classe filep_unique, implémentée à l'aide de la classe hpq du module heapq
    Afin de conserver un comportement FIFO en cas d'égalité des priorités, les éléments en interne sont de la forme (p,pp,e) où p est la priorité, pp une priorité incrémentielle en cas d'insertion avec égalité de p, et e l'élément
    En cas d'insertion d'un élément déjà présent, on met à jour sa priorité si cette dernière est plus basse que la présente.
    """
    def __init__(self):
        self.data=[]

    def __repr__(self):
        return self.chaine_file()

    def est_vide(self):
        """Retourne True si la file est vide, False sinon"""
        return len(self.data)==0

    def index(self,e):
        for i in range(len(self.data)):
            if self.data[i][1]==e:
                return i
        return -1

    def get_max_pp(self,p):
        pp_max=-1
        for e in self.data:
            if e[0]==p and e[1]>pp_max:
                pp_max=e[1]
        return pp_max

    def insere(self,e,p):
        """Ajoute un élément dans la file si il n'y est pas déjà
        Sinon, met à jour sa priorité si jamais p est plus faible
        Retoure si l'élément a réellement été inséré/mis à jour"""
        try:
            assert type(p)==int
            assert p>=0
        except:
            raise Exception('Format de données incorrect')
        ajoute=False
        i=self.index(e)
        if i==-1:
            pp=self.get_max_pp(p)+1
            hpq.heappush(self.data,(p,pp,e))
            ajoute=True
        else:
            if self.data[i][0]>p:

                self.data.pop(i)
                pp=self.get_max_pp(p)+1
                hpq.heappush(self.data,(p,pp,e))
                ajoute=True
        return ajoute

    def enfile(self,e,p):
        """alias de insere"""
        return self.insere(e,p)

    def retire(self):
        """Retire un élément selon la priorité FIFO"""
        try:
            p,pp,a=hpq.heappop(self.data)
        except:
            raise Exception("La file est vide")
        return a,p

    def top(self):
        return self.data[0][2],self.data[0][0]

    def chaine_file(self):
        file_aux=filep()
        s=''
        while not self.est_vide():
            c_e=self.retire()
            s=str(c_e)+'->'+s
            file_aux.enfile(c_e[0],c_e[1])

        while not file_aux.est_vide():
            c_e=file_aux.retire()
            self.enfile(c_e[0],c_e[1])
        return s

    def affiche_file(self):
        print(self.chaine_file)



def genere_file_aleatoire(n,distinct=False):
    from random import randint
    file=file_vide()
    n=min(26,n)
    p=0
    l=[]
    while p<n:
        p+=1
        goOn=True
        while goOn:
            a=randint(65,90)
            if not distinct or chr(a) not in l:
                l.append(chr(a))
                goOn=False
    for e in l:
        file.enfile(e)
    return file


def file_vide():
    return file()

def filep_vide():
    return filep()

def filepu_vide():
    return filep_unique()



from random import random,randint
import numpy as np






class graphe_base:
    def __init__(self):
        self.S=set()
        self.A=set()

    def __repr__(self):
        if self.nombre_sommets()==0:
                return "Ce graphe est vide"
        else:
            if self.nombre_aretes()==0:
                return "Sommets : "+str(self.sommets())+"\nAucune arête."
            else:
                return "Sommets : "+str(self.sommets())+"\nArêtes :"+str(self.aretes())

    def ajout_sommet(self,s):
        """ajoute un sommet au graphe"""
        self.S.add(s)

    def aretes(self):
        """retourne les arêtes du graphe"""
        return self.A

    def sommets(self):
        """retourne le set contenant les sommets"""
        return self.S

    def boucles(self):
        """retourne les sommets de boucles"""
        l=[]
        for a in self.A:
            if a[1]==a[0]:
                l.append(a)
        return tuple(l)


    def contient_sommet(self,s):
        """retourne si un sommet appartient au graphe"""
        return s in self.S


    def degre(self,s):
        """retourne le degré d'un noeud. Lève une exception si le noeud n'appartient pas au graphe"""
        try:
            assert self.contient_sommet(s)
        except:
            raise Exception("Ce sommet n'est pas dans le graphe")

        d=0
        for a in self.A:
            if a[0]==s:
                d+=1
            if a[1]==s:
                d+=1
        return d

    def est_isole(self,s):
        return (self.degre(s)==0)

    def nombre_aretes(self):
        """retourne le nombre d'arêtes"""
        return len(self.A)

    def nombre_sommets(self):
        """retourne le nombre de sommets"""
        return len(self.S)

    def nombre_boucles(self):
        """retourne le nombre de boucles"""
        n=0
        for a in self.A:
            if a[0]==a[1]:
                n+=1
        return n

    def est_complet(self):
        for s1 in self.S:
            for s2 in self.S:
                if s1!=s2 and not self.contient_arete((s1,s2),False):
                    return False
        return True

    def retirer_sommet(self,s):
        """retire un sommet du graphe. Lève une exception si le sommet n'est pas dans le graphe"""
        if self.contient_sommet(s):
            self.S.remove(s)
            for a in self.A:
                if a[0]==s or a[1]==s:
                    self.A.remove(a)
        else:
            raise Exception("Ce sommet n'est pas dans le graphe")

    def est_pondere(self):
        return type(self)==graphe_p or type(self)==graphe_op

    def est_oriente(self):
        return type(self)==graphe_o or type(self)==graphe_op


    def contient_arete(self,a,checkS=True):
        """Vérifie si l'arête est dans le graphe. a est un tuple à deux ou trois éléments, ce qui signifie que cette vérification se fait indépendamment du poids de l'arête"""
        if checkS and not(self.contient_sommet(a[0]) and self.contient_sommet(a[1])):
                return False
        for c_a in self.aretes():
            if self.est_oriente():
                if a[0]==c_a[0] and a[1]==c_a[1] :
                    return True
            else:
                if (a[0]==c_a[0] and a[1]==c_a[1]) or (a[0]==c_a[1] and a[1]==c_a[0]) :
                    return True
        return False

    def voisins(self,s,accessible=True,poids=False):
        """Retourne les voisins d'un sommet s
        Si le graphe est orienté et que le paramètre accessible vaut True, on n'a que les voisins v tels que (s,v) est une arête du graphe
        Si le graphe est pondéré et que poids vaut True, retourne une liste des voisins et le poids de l'arête associé"""
        liste_voisins=[]
        for a in self.A:
            if self.est_oriente() and accessible:
                if a[0]==s:
                    if poids:
                        p=1
                        if self.est_pondere():
                            p=a[2]
                        liste_voisins.append((a[1],p))
                    else:
                        liste_voisins.append(a[1])
            else:
                if a[0]==s:
                    if poids:
                        p=1
                        if self.est_pondere():
                            p=a[2]
                        liste_voisins.append((a[1],p))
                    else:
                        liste_voisins.append(a[1])
                elif a[1]==s:
                    if poids:
                        p=1
                        if self.est_pondere():
                            p=a[2]
                        liste_voisins.append((a[0],p))
                    else:
                        liste_voisins.append(a[0])
        return liste_voisins

    def trace_graphe(self):
        from matplotlib import pyplot as plt
        plt.close('all')
        plt.rcParams['font.size'] = '30'
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid(False)
        ax.axis("off")
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        n=self.nombre_sommets()
        i=0
        dico_S=dict()
        for s in self.sommets():
            #plt.plot(2*np.pi/n*i,1,'go')
            i+=1
            theta=2*np.pi/n*i
            x=np.cos(theta)
            y=np.sin(theta)
            plt.text(x,y,str(s),horizontalalignment='center',verticalalignment='center',backgroundcolor='white')
            dico_S[s]=(x,y,theta)
        for a in self.aretes():
            lx=dico_S[a[0]][0],dico_S[a[1]][0]
            ly=dico_S[a[0]][1],dico_S[a[1]][1]
            if self.est_oriente():
                milieu_x=(2*lx[0]+lx[1])/3
                milieu_y=(2*ly[0]+ly[1])/3
            else:
                milieu_x=(3*lx[0]+2*lx[1])/5
                milieu_y=(3*ly[0]+2*ly[1])/5
            if(self.est_oriente()):
                plt.annotate('',(milieu_x,milieu_y),(lx[0],ly[0]),arrowprops=dict(arrowstyle="->",color='b'),color='b')
            if(self.est_pondere()):
                plt.text(milieu_x,milieu_y,str(a[2]),fontsize="10")
            plt.plot(lx,ly,'b')
        plt.show()




class graphe(graphe_base):
    def ajout_arete(self,a):
        """Ajoute une arête sous la forme d'un tuple de taille 2. Les sommets sont automatiquement ajoutés si ils ne sont pas dans S"""
        try:
            assert type(a)==tuple or type(a)==list
            assert len(a)==2
        except:
            raise TypeError("L'arête doit être un tuple ou une liste de longueur 2")

        self.ajout_sommet(a[0])

        self.ajout_sommet(a[1])

        if(not self.contient_arete(a)):
            self.A.add(a)





    def retirer_arete(self,a):
        """Retire l'arête du graphe. Lève une exception si l'arête n'est pas dans le graphe"""
        if self.contient_arete(a):
            try:
                self.A.remove(a)
            except:
                self.A.remove((a[1],a[0]))
        else:
            raise Exception("Cette arête n'est pas dans le graphe")

class graphe_o(graphe):
    def degrep(self,s):
        """Retourne le degré sortant d'un sommet"""
        try:
            assert self.contient_sommet(s)
        except:
            raise Exception("Ce sommet n'est pas dans le graphe")

        d=0
        for a in self.A:
            if a[0]==s:
                d+=1
        return d


    def degrem(self,s):
        """Retourne le degré entrant d'un sommet"""
        try:
            assert self.contient_sommet(s)
        except:
            raise Exception("Ce sommet n'est pas dans le graphe")

        d=0
        for a in self.A:
            if a[1]==s:
                d+=1
        return d


class graphe_p(graphe_base):
    def ajout_arete(self,a):

        """Ajoute une arête sous la forme d'un tuple de taille 3. Les sommets sont automatiquement ajoutés si ils ne sont pas dans S"""
        try:
            assert type(a)==tuple or type(a)==list
            assert len(a)==3
        except:
            raise TypeError("L'arête doit être un tuple ou une liste de longueur 3")

        self.ajout_sommet(a[0])

        self.ajout_sommet(a[1])
        if not self.contient_arete(a):
            self.A.add(a)



    def poids_arete(self,a):
        """Retourne le poids d'une arête donnée"""
        try:
            assert self.contient_arete(a)
        except:
            raise Exception("Cette arête n'est pas dans le graphe")
        for c_a in self.aretes():
            if (a[0]==c_a[0] and a[1]==c_a[1]) or (a[0]==c_a[1] and a[1]==c_a[0]):
                return c_a[2]



    def retirer_arete(self,a):
        """Retire l'arête du graphe. Lève une exception si l'arête n'est pas dans le graphe.a est un tuple à deux ou trois éléments, ce qui signifie que cette vérification se fait indépendamment du poids de l'arête"""
        dedans=False
        if self.contient_sommet(a[0]) and self.contient_sommet(a[1]):
            for c_a in self.aretes():
                if a[0]==c_a[0] and a[1]==c_a[1]:
                    self.A.remove(c_a)

        raise Exception("Cette arête n'est pas dans le graphe")



class graphe_op(graphe_p):
    def degrep(self,s):
        """Retourne le degré sortant d'un sommet"""
        try:
            assert self.contient_sommet(s)
        except:
            raise Exception("Ce sommet n'est pas dans le graphe")

        d=0
        for a in self.A:
            if a[0]==s:
                d+=1
        return d


    def degrem(self,s):
        """Retourne le degré entrant d'un sommet"""
        try:
            assert self.contient_sommet(s)
        except:
            raise Exception("Ce sommet n'est pas dans le graphe")

        d=0
        for a in self.A:
            if a[1]==s:
                d+=1
        return d

    def poids_arete(self,a):
        """Retourne le poids d'une arête donnée"""
        try:
            assert self.contient_arete(a)
        except:
            raise Exception("Cette arête n'est pas dans le graphe")
        for c_a in self.aretes():
            if (a[0]==c_a[0] and a[1]==c_a[1]):
                return c_a[2]



def genere_graphe_aleatoire(n,oriente=False,boucle=False,taux=0.3):
    """génère un graphe aléatoire à n sommets, n<=26
    paramètres optionnels :
        - oriente : graphe orienté ou non.
        - boucle : dans le cas où le graphe est orienté, autorise les boucles
        - taux : taux d'arête effectivement existantes (si taux=1, toutes les arêtes possibles existent, ce qui correspond au graphe Kn
        """
    if(oriente):
        G=graphe_o()
    else:
        G=graphe()
    try:
        assert n<=26
    except Exception as e:
        print("Trop de sommets")

    for i in range(n):
        s=chr(65+i)
        G.ajout_sommet(s)

    if(oriente):
        for s in G.sommets():
            for ss in G.sommets():
                if (random()<taux and (boucle or s!=ss)):
                    G.ajout_arete((s,ss))
    else:
        S2=G.sommets().copy()
        while len(S2)>0:
            s=S2.pop()
            for ss in S2:
                if (random()<taux ):
                    G.ajout_arete((s,ss))
    return G

def genere_graphe(n):
    G=genere_graphe_aleatoire(n)
    return G


def genere_graphe_p_aleatoire(n,oriente=False,boucle=False,taux=0.3,poidsmax=100, poidsmin=0):
    """génère un graphe pondéré aléatoire à n sommets, n<=26
    paramètres optionnels :
        - oriente : graphe orienté ou non.
        - boucle : dans le cas où le graphe est orienté, autorise les boucles
        - taux : taux d'arête effectivement existantes (si taux=1, toutes les arêtes possibles existent, ce qui correspond au graphe Kn
        - poidsmax : valeur maximale du poids d'une arête. Si poidsmax est plus petit que poidsmin, il vaudra poidsmin.
        - poidsmin : valeur maximale du poids d'une arête. Si poidsmin est négatif ou nul, il est remis à 1.
        """
    poidsmin=max(1,poidsmin)
    poidsmax=max(poidsmax,poidsmin)
    if(oriente):
        G=graphe_op()
    else:
        G=graphe_p()
    try:
        assert n<=26
    except Exception as e:
        print("Trop de sommets")

    for i in range(n):
        s=chr(65+i)
        G.ajout_sommet(s)
    if(oriente):
        for s in G.sommets():
            for ss in G.sommets():
                if (random()<taux and (boucle or s!=ss)):
                    G.ajout_arete((s,ss,randint(poidsmin,poidsmax)))
                    #print("ajout arete",s,ss)
    else:
        S2=G.sommets().copy()
        while len(S2)>0:
            s=S2.pop()
            for ss in S2:
                if (random()<taux):
                    G.ajout_arete((s,ss,randint(0,poidsmax)))
    return G

def graphe_from_liste_aretes(l,oriente=False):
    """génère un graphe depuis la liste des arêtes
    Le paramètre oriente décide si le graphe est considéré comme orienté ou non
    """
    if(oriente):
        G=graphe_o()
    else:
        G=graphe()
    for a in l:
        G.ajout_arete(a)
    return G

def graphe_p_from_liste_aretes(l,oriente=False):
    """génère un graphe depuis la liste des arêtes
    Le paramètre oriente décide si le graphe est considéré comme orienté ou non
    """
    if(oriente):
        G=graphe_op()
    else:
        G=graphe_p()
    for a in l:
        G.ajout_arete(a)
    return G

def graphe_vide(oriente=False,pondere=False):
    if oriente and pondere:
        G=graphe_op()
    elif pondere:
        G=graphe_p()
    elif oriente:
        G=graphe_o()
    else:
        G=graphe()
    return G

def compare_graphes(G1,G2):
    if type(G1)!=type(G2):
        print('Les types sont différents')
        return False
    if G1.sommets()!=G2.sommets():
        print('Sommets différents')
        return False
    if len(G1.aretes())!=len(G2.aretes()):
        print("Nombre d'arêtes différent")
        return False
    for a1 in G1.aretes():
        if not G2.contient_arete(a1):
            print(str(a1)+' est manquante dans G2')
            return False
    return True

if __name__ == "__main__":
    def test_pile():
        print("\n--- Test de la pile ---")
        P = pile_vide()
        for e in ['A', 'B', 'C']:
            P.empile(e)
            print(f"Empilé : {e}")
        print("Contenu de la pile :")
        P.affiche_pile()
        print("Dépile :", P.depile())
        print("Sommet (top) :", P.top())
        print("Pile après opérations :")
        P.affiche_pile()

    def test_file():
        print("\n--- Test de la file ---")
        F = file_vide()
        for e in ['A', 'B', 'C']:
            F.enfile(e)
            print(f"Enfilé : {e}")
        print("Contenu de la file :")
        F.affiche_file()
        print("Retiré :", F.retire())
        print("Tête :", F.top())
        print("File après opérations :")
        F.affiche_file()

    def test_file_prioritaire():
        print("\n--- Test de la file de priorité ---")
        F = filep_vide()
        F.insere("Tâche faible", 5)
        F.insere("Tâche moyenne", 3)
        F.insere("Tâche urgente", 1)
        print("Contenu de la file de priorité :")
        F.affiche_file()
        print("Retiré :", F.retire())
        print("Tête :", F.top())

    def test_filep_unique():
        print("\n--- Test de la file de priorité unique ---")
        F = filepu_vide()
        F.insere("A", 5)
        F.insere("B", 3)
        F.insere("C", 1)
        F.insere("A", 2)  # Mise à jour car priorité meilleure
        print("Contenu de la file unique :")
        F.affiche_file()
        print("Retiré :", F.retire())
        print("Tête :", F.top())

    def test_graphe():
        print("\n--- Test de graphe aléatoire ---")
        G = genere_graphe_aleatoire(6, oriente=False, taux=0.5)
        print(G)
        print("Trace graphique du graphe...")
        G.trace_graphe()

    def test_graphe_p():
        print("\n--- Test de graphe pondéré aléatoire ---")
        G = genere_graphe_p_aleatoire(6, oriente=True, taux=0.4, poidsmin=1, poidsmax=10)
        print(G)
        print("Trace graphique du graphe pondéré orienté...")
        G.trace_graphe()

    def menu():
        while True:
            print("\n==== MENU TEST TD_07_aux ====")
            print("1 - Tester les piles")
            print("2 - Tester les files")
            print("3 - Tester les files de priorité")
            print("4 - Tester les files de priorité unique")
            print("5 - Générer un graphe simple")
            print("6 - Générer un graphe pondéré orienté")
            print("0 - Quitter")
            choix = input("Choix ? ")
            if choix == "1":
                test_pile()
            elif choix == "2":
                test_file()
            elif choix == "3":
                test_file_prioritaire()
            elif choix == "4":
                test_filep_unique()
            elif choix == "5":
                test_graphe()
            elif choix == "6":
                test_graphe_p()
            elif choix == "0":
                break
            else:
                print("Option inconnue.")
    menu()