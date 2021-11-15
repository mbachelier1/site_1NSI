# Les tuples
Un tuple, ou n-uplet, est un type données Python constitués d'éléments séparés par des virgules, et encadrés par des parenthèses. Un tuple ressemble à une liste, mais un tuple n'est pas modifiable (ni insertion ni suppression ni remplacement de valeurs).  
La syntaxe diffère des listes en utilisant les paranthèses au lieu des crochets.  
```python
a=(3,4) #a est un tuple contenant les valeurs 3 et 4

u,v=a #permet de récupérer séparément les valeurs contennues dans a
#u sera égal à 3 te v à 4

(b,c) = (5,6) #b sera égal à5 et c à 6
```
Si on essaye de supprimer par exemple : 
```python
a.remove(3)
#si on essaye de supprimer une valeur le programme renvoie une erreur
```
Les tuples sont utilisés lorsque l'on souhaite que les données ne soient pas modifiables par erreur.

---------
# Les dictionnaires
un dictionnaire est une collection de valeurs, un peu comme une liste sauf que les valeurs ne sont pas ordonnées mais associées deux à deux. Chaque valeur du dictionnaire correspond à une clé. Par exemple : 
```python
nb_pneus={"voiture" : 4,"vélo" : 2,"tricycle" : 3}
```
Voici un dictionnaire qui associe la valeur 4 aux voitures, 2 aux vélos, ...  
"voiture", "vélo", "tricycle" sont les clés du dictionnaire et 4, 2 et 3 sont les valeurs correspndant aux clés.

## Ajouter, modifier et supprimer un élément
On peut créer un dictionnaire vide `dico={}` puis ajouter des valeurs au fur et à mesure avec la syntaxe `dico[cle]=valeur`.  
```python
dico={}
dico["maths"]=12
print(dico)

>>> # script executed
{'maths': 12}
>>> 
```

une fois créée, on peut modifier cette valeur :
```python
dico={}
dico["maths"]=12
print(dico)
dico["maths"]=20
print(dico)

>>> # script executed
{'maths': 12}
{'maths': 20}
>>> 
```

ou la supprimer :
```python
dico={}
dico["maths"]=12
print(dico)
dico["NSI"]=14
print(dico)
del(dico["maths"])
print(dico)

>>> # script executed
{'maths': 12}
{'maths': 12, 'NSI': 14}
{'NSI': 14}
>>> 
```

## Accéder aux éléments d'un dictionnaire
Nous allons partir de ce dictionnaire :
```python
moyennes={"maths" : 12, "NSI" : 14, "Anglais" : 8, "Histoire" : 18}
```
### Accéder à la valeur correspndant à une clé
Pour récupérer la valeur correspondant à la clé "NSI" par exemple :  
```python
print(moyennes["NSI"])

>>> # script executed
14
>>> 
```
### Accéder à la liste des clés
```python
print(moyennes.keys())

>>> # script executed
dict_keys(['maths', 'NSI', 'Anglais', 'Histoire'])
>>>
```
On constate que l'on a QUE LES CLES et sous la forme d'un objet un peu spécial non manipulable.  
Pour utiliser cette liste nous allons la convertir en liste avec la méthode `list`.

```python
print(list(moyennes.keys())

>>> # script executed
['maths', 'NSI', 'Anglais', 'Histoire']
>>> 

```

### Accéder à la liste des valeurs
Comme pour les clés, nous allons convertir en liste le résultat :

```python
print(moyennes.values())
print(list(moyennes.values()))

>>> # script executed
dict_values([12, 14, 8, 18])
[12, 14, 8, 18]
>>> 
 
```
### Accéder à la liste des couples (clé,valeur)
Les couples (clé,valeur) sont appelés les `items` d'un dictionnaire. La fonction `items()` permet de les réupérer sous forme de tuples et nous allons encore une fois les ranger dans une liste pour plus de facilités.
```python
print(moyennes.items())
print(list(moyennes.items()))

>>> # script executed
dict_items([('maths', 12), ('NSI', 14), ('Anglais', 8), ('Histoire', 18)])
[('maths', 12), ('NSI', 14), ('Anglais', 8), ('Histoire', 18)]
>>> 
```

## Autres méthodes
Voici une liste non-exhaustive des méthodes les plus utiles :  

- `dico.get (k)`: permet d'accéder à la valeur dont la clé est k dans le dictionnaire dico
- `dico.items()` : liste les items du dictionnaire
- `dico.values()` : liste les valeurs du dictionnaire
- `dico.pop(k)` : supprime l'item dont la clé est k du dictionnaire dico mais récupère la valeur supprimée contrairement à del
- `dico.keys()` : liste les clés du dictionnaire

!!! note "NB"
	Les méthodes keys, items, et values renvoient un objet que l'on peut transformer en liste par :  
	`list(nombre_de_roues.values())`
