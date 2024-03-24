#exercice 1
import datetime
dateHeure = lambda : datetime.datetime.today()
print (dateHeure())

#exercice 2
def triple(n):
    return n*n*n
def triplerListe(*l):
    print(list(map(triple, l)))
triplerListe(1,2,3)

#items = [1,2,3,4,5,6]
#print(list(map(lambda x : x*x*x, items)))

#exercice 3:

chaine=tuple("ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG")
print("premiere sequence ", chaine)
list_mot=[]
i=0
while(i<=len(chaine)-2):
    list_mot.append(chaine[i]+chaine[i+1])
    i=i+2
print(list_mot)

for mot in list_mot:
    print(mot, list_mot.count(mot))
    list_mot.remove(mot)



#exercice 4
list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre',
'Novembre', 'Décembre']
list3=[]
for i in range(len(list1)):
    list3.append(list2[i])
    list3.append(list1[i])
print(list3)


#exercice 5
chaine = input("Saisir la chaine")

def minMax(chaine):
    nbmaj = 0
    nbmin = 0
    for i in chaine:
        if i.islower():
            nbmin+=1
        else:
            nbmaj+=1
    print("nbmaj:", nbmaj)
    print("nbmin:", nbmin)

minMax(chaine)


# exercice 6
chaine =  input("Entrez une chaine : ")
c=""
for i in chaine :
    if  ( i.isalnum()) :
        c+=i
print(c)


#exercice 7
chaine ="l’effffort est immmense"
chaine=list(chaine)
for i in range(len(chaine)-3):
    if chaine[i]==chaine[i+1] and chaine[i]==chaine[i+2]:
        j=i
        while chaine[j]==chaine[j+1] and j<len(chaine)-3:
            chaine.remove(chaine[j])
            j=j+1
print(str("%s"%''.join(chaine)))





# exercice 8
chaine = input("Entrez une chaine ")
chaine=list(chaine)
for i in range(len(chaine)):
    if chaine[i]=="a":
        chaine[i]="q"
    elif chaine[i]=="q":
        chaine[i]="a"
    elif chaine[i] == "z":
        chaine[i] = "w"
    elif chaine[i] == "w":
        chaine[i] = "z"
print(str('%s'%''.join(chaine)))


#exercice 9
import math


def f(x,y):
    if(x>y):
        return math.pow(x,2)-x*y+3
    elif(x<y):
        return math.pow(y,2)+x-2
    else  :return y

x=float(input('entrez x'))
y=float(input('entrez y'))
print("la valuer de la fonction f pour x= " +str(x)+ "et y= "+ str(y)+ "est " +str(f(x,y)))