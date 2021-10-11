import pickle

#ouverture du fichier
f=open('dep.txt','rb')
#chargement du contenu du fichier dans la variable Dept
Dept=pickle.load(f)
f.close()

print(Dept)