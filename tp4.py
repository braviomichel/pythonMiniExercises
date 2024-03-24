#exercice 1
class CompteurList:
    listElement=[]
    def compter(self):
        return len(self.listElement)
    def ajoutElement(self, element):
        self.listElement.append(element)
    def delRedondant(self):
        return list(set(self.listElement))



#exercice 2
class L:
    def renvoieList(self, chemin):
        fichier=open(chemin,'r')
        if fichier:
            l=fichier.read()
            return l
        else: print("erreur")
    def compterMots(self, chaine, chemin):
        d={}
        freq=0
        l=self.renvoieList(chemin)
        l=str(l)
        for mot in l:
            if mot==chaine:
                freq=freq+1
        d["frequence"]=freq
        d["chaine"]=chaine
        return d
chemin='input.txt'
liste=L()
print(len(liste.renvoieList(chemin)))
print(liste.compterMots("un", chemin))




#exercice 3
class Strr:
    def get_String(self, chaine):
        self.string=chaine
    def print_String(self):
        print(self.string.upper())

c=Strr()
c.get_String("aller")
c.print_String()



#exercice 4
import math


class Circle:
    def __init__(self,rayon):
        self.__rayon=rayon
    def aire(self):
        return (math.pi*math.pow(self.__rayon,2))
    def perimetre(self):
        return (2*self.__rayon*math.pi)
cercle=Circle(5)
print(cercle.aire(), cercle.perimetre())




#exercice 5
class Rectangle:
    def __init__(self, longueur, largeur, nom="rectangle"):
        self.longueur=longueur
        self.largeur=largeur
        self.nom=nom
    def __str__(self):
        return "longueur= {}, largeur= {}, nom={} ".format(self.longueur,self.largeur,self.nom)
    def surface(self):
        return self.largeur*self.longueur

class Carre(Rectangle):
    def __init__(self,cote):
        super().__init__(cote, cote,"carre")

rectangle=Rectangle(4,5)
print(rectangle)
carre=Carre(5)
print(carre)






#exercice 6
class Salarie:
    def __init__(self, matrcule, nom,salaire):
        self.__matricule=matrcule
        self.__nom=nom
        self.__salaire=salaire
    def CalculSalaireAnnuel(self):
        return (self.__salaire*1.2)*12
    def affichage(self):
        print("Matricule = {}, nom={}, salaireAnnuel ={}".format(self.__matricule,self.__nom, self.CalculSalaireAnnuel()))

class Commercial(Salarie):
    def __init__(self,matricule,nom, salaire,ca,taux):
        super().__init__(matricule,nom,salaire)
        self.__ca=ca
        self.__taux=taux
    def CalculSalaireAnnuel(self):
        return super().CalculSalaireAnnuel() + self.__ca*(self.__taux/100)
    def affichage(self):
        super().affichage()
        print("ca={:f}, taux={:f}".format(self.__ca,self.__taux))
s=Salarie(1,"ali",5000)
s.affichage()
c=Commercial(2,"driisi",8000,500,1.5)
c.affichage()