# Fonctions et spécifications
## Créer une fonction
Pour ne pas répéter plusieurs fois la même série de calculs dans un programme, on peut définir une fonction qui à chaque fois qu'on l'éxécutera, répètea les instrucions qu'elle contient.  

!!! example "Le prof d'EPS"
	Pour ne pas répéter plusieurs fois les consignes de courses, un prof d'EPS définit la fonction *courir_sur(distance,eleve)* distance pourra changer de valeur en fonction des élèves (100m, 200m ou 400m).

	La fonction courir_sur(distance,eleve) consiste à :

	- élève s'échauffe en trotinnant sur 3 tours de piste
	- élève reprend son soufle et s'étire
	- élève se rend sur la ligne de départ
	- quand le starter retentit élève court le plus vite poussible sur distance
	- élève vient annoncer son temps au professeur.

	Une fois la fonction définie le prof n'a plus qu'à dire à certains élèves *courir_sur(100m,Juliette)* ou *courir_sur(200m,Arthur)* sans avoir à répéter les consignes.  
	La valeur de distace et le nom de l'élève sont appelés `paramètre` ou `argument`de la fonction, et la valeur retournée (le temps) dépend à la fois du paramètre distance mais aussi de l'élève.


En python pour définir une fonction on utilise le mot clé `def` suivi du nom de la fonction et des paramètres. Pour la valeur calculée on utilisera le mot clé `return`. 

```python
def ma_fonction(arg1,arg2): 
# ma_fonction va utiliser deux arguments arg1 et arg2 qui pourront avoir des valeurs différetes à chauqe appel
	resultat=arg1+arg2 #on additionne les deux paramètres
	return resultat # on retourne le résultat
#on exécute la fonction
a=ma_fonction(2,3) # a prend la valeur du résultat de la fonction soit 5
b=ma_fonction('coucou','toi') #b prend la valeur du résultat soit 'coucoutoi'
#on affiche les résultats
print(a)
print(b)
```
!!! caution "Attention"
	Si le professeur explique la fonction aux élèves mais que jamais il ne l'utilise, personne ne courra. Il faut `appeler`la fonction pour qu'elle s'éxécute.

!!! note "Remarque"
	on peut exécuter la fonction avec un `print(ma_fonction(2,3))` qui affichera le résultat mais ne le retiendra pas. Si on écrit simplement `ma_fonction(2,3)` la fonction sera exécutée mais le résultat ne sera pas affiché ni mémorisé.

## Fonction sans valeur de retour et/ou sans arguments
Une fonction qui ne renvoie pas de valeur est appelée **procédure** elle a une simple fonction d'affichage. 


<iframe id="inlineFrameExample"
    title="Inline Frame Example"
 	width="100%"
    height="400"
    src="https://console.basthon.fr/?script=eJxNjsEOwiAMhu8kvEPNDrB40Xgz7rI3abay1QxYGOjri0zFnpq_7fe12dBt8MCFUoCRIFD0KUgxkgE0hocZJwJtfWyvUkCuNbCLJZBCit-OVr1393yrSt4ULoYpWXJx5w3erjF79BfF3WlvnjMvBHy7fAbVw21NuOPj-f8JZdjx4S2s6Bd9STp5">
</iframe>
La fonction `compteur()` sans argument s'éxécutera toujours de la même façon. 

!!! caution "Affichage de la valeur"
	Si on uilise l'instruction `print(compteur())` le programme retournera `None`. En effet, l'instruction `print` pour une fonction a pour effet d'afficher la valeur retournée par l'instruction `return`, or ici il n'y en a pas.

## Portée d'une variable
Une variable est appelée **locale** lorsqu'elle n'est utilisée que dans la fonction. Le programme principal ne reconnait pas la variable. Si elle est définie dans tout le programme elle est appelée variable **globale**.  
```python
def vol_sphere(r):
	cube=r*r*r
	vol=4*cube*3.14/3
	return vol

v=vol_sphere(3)
print(cube)
```
![variable locale](img/erreur_cube.PNG)

La variable `cube` est définie DANS la fonction et n'est donc pas reconnu par le programme principal. v est définie dans le programme principale, elle sera reconnue partout, c'est une variable globale.

!!! danger "Attention aux confusions"
	```python
	a=15
	def calcul(nb):
		a=12
		return nb+a
	print(calcul(2)) #renvoie le calcul fait avec a=12
	print(a) #renvoie 15
	```  
	a=15  variable globale valable dans tout le programme sauf dans la fonction.  
	a=12 est une variable locale valable que dans la fonction.   
	**ATTENTION : Ne pas nommer de la même façon deux variables!**  

## Structurer son script
![strucuturer son script](https://courspython.com/_images/structure_programme.png)
Le programme commence à être long, il faut ranger:  
On définit le format de codage du texte :

```python
# -*- coding: utf-8 -*- 
# coding : utf-8
```

Importer les fonctions de modules externes
```python
from math import cos,pi
```

Définition de vos fonctions
```python
Def ma_fonction(arg1,arg2):
	return arg1+arg2
```
Corps principal du programme
*main*
 
Le code est TRES long?!  
On utilise plusieurs fichiers et on les importe comme une bibliothèque normale  

![test](img/module.PNG)
![main](img/module2.PNG)

Plusieurs possibilités d’import dans main :
```python
from tests import affiche
affiche()

import tests
tests.affiche()

import tests as ts
ts.affiche()
```


## Conventions

`nom_de_ma_fonction`: pour les fonctions, variables et méthodes tout en minuscule avec _ pour séparer les mots.

`MaClasse`: pour le nom des classes (en terminale). Majuscule pour chaque nouveau mot et mots collés. 

Les constantes sont entièrement en majuscule: `NOM_DE_MA_CONSTANTE`. Une constante est une variable à laquelle on donne une valeur qui ne changera pas dans tout le programme. 


## Documenter une fonction
Le `docstring` se place juste après la création de la fonction par `def`. Il commence et termine par trois guillemets ".
Le  docstring doit contenir :  

- La descripton et le rôle de la fonction  
- les paramètres passés en arguments (type et rôle)  
- le type de ce qui est retourné  

Ce docstring, peut être lu en tapant:  
`help(nom_de_ma_fonction)`   
Ou   
`nom_de_ma_fonction.__doc__`   

![Documenter la focntion](img/documenter.PNG)
![Accéder à la documentation de la focntion](img/res_documenter.PNG)  
Très utile lorsque le code est réutilisé ensuite par quelqu’un d’autre.

## Tester une fonction

### Tests unitaires
Ils permettent de savoir si une fonction est correctement implémentée. On vérifie notamment les valeurs limites, les cas particuliers et les erreurs.
On les place dans la docstring.  
Créer des tests unitaires :
![créer des tests unitaires](img/test_unitaires.PNG)  
En cas d’erreur (un test n’est pas exécuté correctement).  
On modifie le code précédet en remplaçant le résultat de carré(2) par 3 au lieu de 4 pour générer une erreur.  
Ici, un test sur 3 de la fonction carré ne renvoie pas ce qu’on attend:   
![erreur des tests unitaires](img/res_test_unitaire.PNG)


### Assertions
On souhaite ici que la fonction calcule la somme de deux entiers et uniquement des entiers. Il va donc falloir vérifer que l'utilisateur en entrer des entiers :
```python
def somme(x,y):
	assert(isinstance(x,int))
	assert(isinstance(y,int))
	s=x+y
	return s
	print(somme(1,2.2))
```
Une assertion (mot clé `assert`) permet de vérifier si une condition est respectée à un moment du code. Ici on vérifie que x et y sont des entiers avant de faire le calcul.
![erreur assertion](img/erreur_assert.PNG)
Ici une erreur d'assertion est détectée puisque y est un flottant.  
Avantage sur tests unitaires :

- Permet de placer des tests en cours de fonction et pas seulement sur le résultat
- Permet de donner un message différent selon l’erreur détectée


Par exemple, on demande son age à l'utilisateur. On s'attend à ce qu'il entre un nombre positif. On va donc tester si c'est un nombre et s'il est positifi avec des messages d'erreur adaptés.

```python
age=input('quel est ton age? ')
try : 
	#bloc à tester
	age=int(age) #on converti en entier
	assert age>=0
except ValueError:
	#bloc à executer en cas de détectiion d'une erreur lié à la valeur
	print('on demande un nombre')
except AssertionError:
	#bloc à executer si l'assertion lève une erreur
	print('on veut un nombre positif SVP!')
else :
	#aucune erreur détectée
	print(f'tu as {age} ans')
finally :
	# à exécuter quoiqu'il arrive
	print('merci d\'avoir joué!')

```
Ce bloc permettra de tester les entrées de l'utilisateur lors de programmes plus complexe.

??? example "Tester des entrées sans sortir du programme"
	Tant que l'age entré ne sera pas un entier positif, le programme continue de proposer d'entrer une valeur.
	```python
	ok=True
	while ok: #tant que l'on a pas validé l'entrée
	    age=input('quel est ton age? ')
	    try : 
	        age=int(age) 
	        assert age>=0
	    except ValueError:
	        print('on demande un nombre')
	    except AssertionError:
	        print('on veut un nombre positif SVP!')
	    else :
	        #aucune erreur détectée
	        print(f'tu as {age} ans')
	        ok=False #l'entrée est validée on sort de la boucle while
	```