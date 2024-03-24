#exercice 1
fichier= open('out.txt', 'w')
with open('input.txt','r') as f :
    for line in f.readlines():
        if line[0]!='#':
            fichier.writelines(line)
f.close()
fichier.close()

# exercice 2
import csv

#exercice 2
import csv
with open('Produits.CSV', newline='') as f:
    lire = csv.reader(f)
    for ligne in lire:
        print(ligne)

# exercice 3
import csv

data = csv.DictReader(open('Produits.csv'))
print("CSV en fichier format dico")
for row in data :
    print((row))



# exercice 4
import sqlite3
conn = sqlite3.connect('dbpython.db')
print("ouverture de base de données reussie")
sql = """CREATE TABLE Produit(
    RefProduit CHAR(20), Nfournisseur int, 
    CodeCateg int, QuantiteUnite char(40),
    PrixUnite float, UniteStock int,
        UniteCmd int,NiveauReap int, Indisponible char(4)
    )"""
conn.execute(sql)
print("table cree avec succes")
sql = """CREATE TABLE categorie(
    CodeCateg int, NomCateg char(20), Description char (400)
)"""

conn.execute(sql)
print("reusi")
conn.commit()
conn.close()
