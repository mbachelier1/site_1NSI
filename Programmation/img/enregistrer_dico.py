import pickle
#le dictionnaire que l'on souhaite sauvegarder
departement={36:'Indre',30:'Gard',75:'Paris'}
#on ouvre un fichier dont le nom est dep (il sera créé s'il n'existe pas) et on le place dans une variable appelée fichier
fichier=open('dep.txt','wb')
#on enregistre le dictionnaire dans le fichier 
pickle.dump(departement,fichier)
#on ferme le fichier
fichier.close()

