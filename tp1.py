# exercice 1
n= input("Entrez un entier positif : ")
print(type(n))
if int (n) % 2 == 0:
    print("Pair")
else:
    print("IMPAIR")

#exercice 2
liste = ['ISE', 'IMIAE', 'GM', 'GBM', 'EEIN', 'INDIA']
for i in liste :
    print(i, len(i))

#exercice 3
from builtins import min

l = [18,13, 12.5, 46, 27.5, 52, 10]
l2 = []
while l:
    l2.append(min(l))
    l.remove(min(l))
print(l2)


#exercice 4
liste=[7, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
for i in liste:
    while(liste.count(i)!=1):
        liste.remove(i)
liste.sort()
print(liste)


#exercice 5

n=0
l=[]
while n >= 0:
    n = input("Entrez la note")
    n = int(n)
    l.append(n)
    for i in l:
        print ("Nombre de notes entrées" +str(len(l)))
        print("Note max!: " + str(max(l)))
        print ("Note min : " + str(min(l)))
        print("Moyenne : "+ str(sum(l)/len(l)))
    print(l)

#exercice 6

chaine = input ("Entrez une chaine \n")
mot = input("Enntrez un mot \n")
print(chaine.find(mot))

#exercice 7
def somme (*l):
    return sum(l)
print (somme(2,3,4,5))

#exercice 10
def liste_unique(liste):
    for i in liste:
        while(liste.count(i)!=1):
            liste.remove(i)
    print(liste)
#on peut utiliser la fonction set()

#exercice 11
def concatDictionnaire(dict1, dict2) :
    dict3={}
    for value in dict1 :
        dict3[value]=dict1[value]
    for value in dict2 :
        dict3[value]=dict2[value]
    print(dict3)

dict1={'aller':10,'ici':20}
dict2={'alla':40,'imi':70}

concatDictionnaire(dict1,dict2)


#exercice 12
ajout = lambda x:  x+10
print(ajout(5))

print(ajout(15))

#exercice 13
a= lambda x,y : x*y
print(a(2,3))


#exercice 14
b=lambda l : l.sort
