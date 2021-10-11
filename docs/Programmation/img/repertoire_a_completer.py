#impotation des modules
import pickle
import os.path

#definition des fonctions
def ajouter_entree(repertoire):
    """ajoute dans le dictionnaire passé en argument l'entree {nom:num}
    dont a clé et la valeur sont entrées par l'utilisateur
    la fonction affiche une chaine formatée 'le contact {} dont le numéro est {} a été ajouté'
    ou 'le contact existe deja {} ' en cas de traitement du BONUS
    """
    ...

    
    
def supprimer_entree (repertoire):
    '''supprime du dictionnaire passé en argument l'item dont la clé
    est entrée par l'utilisateur. La fonction doit afficher 'le contact existe deja {} '
    ou 'le contact {} a été supprimé''''
    ...
        

def trouver_num(repertoire):
    '''retourne la valeur correspondant à la clé donnée par
    l'utilisateur dans le dictionnaire passé en argument. La focntion affiche 'le numéro que vous recherchez est : {}'
    ou 'ce contact n\'existe pas!''''
    ...
    
def afficher_repertoire(repertoire):
    '''affiche la totalité du repertoire sous forme nom:numero'''
    ...
        

##### MAIN ######

################################### NE PAS TOUCHER ################################
#on vérifie si le fichier existe ou non
if os.path.isfile('repertoire.txt'):
    #s'il existe on le charge et on copie son contenu dans le dictionnaire contacts
    File=open('repertoire.txt', "rb")
    contacts=pickle.load(File)
    File.close()
else:
    #sinon on initialise le dictionnaire contact avec le numéro des pompiers
    contacts={'Pompiers':'18'}
    fichier=open('repertoire.txt','wb')
    #on enregistre le dictionnaire dans le fichier 
    pickle.dump(contacts,fichier)
    #on ferme le fichier
    fichier.close()
        
################################################################################
        
## A VOUS##

##Ouvrir le fichier 'repertoire.txt' en mode rb et charger son contenu

if __name__=='__main__':
    ##créer la boucle d'actions
    ...
    ##sauvegarder le dictionnaire dans le fichier 'repertoire.txt' en mode wb
    ...

