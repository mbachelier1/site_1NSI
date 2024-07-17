# Coût temporel d'un programme


## Qu'est ce que la compléxité?
Le problème de la complexité temporelle (le temps mis par le programme pour s'executer) est fondamental en informatique. Sur un petit exercice contenant seulement 20 valeurs, les ranger dans l'ordre croissant sera très rapide quelque soit la méthode. Mais s'il faut répéter cela des milliers de fois ou que la taille de la liste est de 50000 valeurs, la qualité de l'algorithme est très importante. Entre l'algorithme le plus performant et le moins performant nous aurons un écart de 15 fois meilleur (dans le pire des cas) pour 20 valeurs et de 10640 fois pour 50000 valeurs! 

Pour évaluer la complexité d'un algorithme on calcule le nombre d'étapes (comparaisons, calculs, affectations) nécessaires pour n données.

!!! note "Remarque"
	On peut aussi étudier compléxité spatiale qui correspond à la place occupée en mémoire par le programme. Cette part de la complexité ne sera pas abordée. Lorsque l'on parlera de complexité il s'agira de compléxité temporelle.  

## Recherche d'élément dans un tableau
Evidemment selon les cas, le nombre d'opérations à effectuer sera différent si l'élément se trouve en premier dans le tableau, ou s'il se trouve en dernier, ou encore s'il n'y est pas du tout. On s'interessera toujours donc à la complexité **dans le pire des cas** mais sachez que l'on peut étudier aussi la complexité d'un cas moyen (plus difficile à appréhender).  

Nous considèrerons que chaque ligne de code est une opération à comptabiliser :  
 - une comparaison `if a<2` est une opération  
 - un affichage (`print(2)`) est une opération  
 - une lecture d'entrée `input()`  
 - un accès à la mémoire `print(somme)` correspond à deux  opérations car on accède à la variable `somme`  et on l'affiche
 - un calcul `2+3` est une opération  
 - une itération : lorsque l'on fait `for i in range (10)` on fait 10 fois l'augmentation de i puis ce que contient le bloc  
 - une opération booléenne  
 - une instruction `return` constitue une opération  


!!! warning "Attention"
	- `if a<2 and b==3` correspond à 3 opérations (2 compraison et une opération booléenne) 
	- `somme = somme+4` contient une affectation, un calcul et un acès à la mémoire soit 3 opérations
	- `a=input()` constitue 2 opérations (affectation et lecture)  
	- `else`ne constitue pas une opération car il n'y a pas de comparaison



!!! question "Parcourt d'un tableau"
	Lorsqu'on parcourt un tableau pour lire toutes les valeurs, combien d'actions fait-on si on a 20 éléments dans le tableau ?

	=== "Algorithme"
		```pseudocode
		VARIABLES
		tab ← tableau de 20 valeurs
		DEBUT
		Pour i allant de 0 à 19 :
	    	afficher tab[i]
		fin pour
		FIN
		```
		<div id="text">
	  	<form>
		    <input style="border : solid 1px; border-radius : 2px;" type="text" name="reponse" maxlenght="15" id="reponse1" autocomplete="off">
		    <input type='button' style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" onclick="reactionText1()" value="Vérifier">  <input id="bouAffText1" type="button" onclick="AfficheText1()" value="Correction" style="display:none;"><br> 
			</form>
		     <div style="font-weight: bold;" id="messageText1"></div>
		     <div id="correctionText1" style="display:none;"> <p> Voir les explications</p></div>
		</div>

	=== "Explications"
		- ligne 4 : itération de i  :arrow_right: 1  
		- ligne 5 : accès à la mémoire :arrow_right: 1  
		- Ces deux lignes seront répétées 20 fois  
		- 2*20 = 40 opérations


!!! question "et pour n cases?"
	Si le tableau que l'on parcourt possède n cases.
	<div id="text">
	  	<form>
	    <input style="border : solid 1px; border-radius : 2px;" type="text" name="reponse" maxlenght="15" id="reponse2" autocomplete="off">
	    <input type='button' style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" id="BoutonValider" onclick="reactionText2()" value="Vérifier">  <input id="bouAffText2" type="button" onclick="AfficheText2()" value="Correction" style="display:none;"><br>  
		</form>
     <div style="font-weight: bold;" id="messageText2"></div>
     <div id="correctionText2" style="display:none;"> <p> Si on fait 2 instructions par case, on aura le double d'actions que de cases soit 2n étapes.</p></div>
	</div>

Ici, le nombre d'opérations est proportionnel à n. On dit que la compléxité est **linéaire** et on l'écrit **$O(n)$**.

!!! note "A noter"
	On peut trouver un nombre d'opérations $3\times n+4$ ou encore $2\times n+1$, on sera toujours dans le cas d'une compléxité linéaire car on a toujours un nombre d'opérations proportionnelles à n.


Voici un algorithme de recherche d'un élément dans un tableau.
```PSEUDOCODE
	VARIABLES
	tab : tableau de longueur n
	e : entier
	DEBUT
		i <- 1
		n <- longueur du tableau
		TANT QUE i<=n :
			SI tab[i]=e:
				RENVOYER VRAI
			SINON :
				i=i+1
			FIN SI
		FIN TANT QUE
		RENVOYER FAUX
	FIN
```
Appliquer l'algorithme **à la main** pour un tableau de 10 valeurs puis extrapoler à n valeurs. Le pire des cas ici est que l'élément n'est pas dans le tableau.  

!!! question "Formuler la compléxité"
	Exprimer la complexité sous la forme $2n+4$.  
	<div id="text">
	  	<form>
	    <input style="border : solid 1px; border-radius : 2px;" type="text" name="reponse" maxlenght="15" id="reponse3" autocomplete="off">
	    <input type='button' style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" id="BoutonValider" onclick="reactionText3()" value="Vérifier">  <input id="bouAffText3" type="button" onclick="AfficheText3()" value="Correction" style="display:none;"><br>  
		</form>
     <div style="font-weight: bold;" id="messageText3"></div>
     <div id="correctionText3" style="display:none;"> <p> On repète n fois la comparaison du TANT QUE, celle du SI, l'incrémentation de i et on ajoute le renvoi et les deux affectations. </p></div>
	</div>


Si on reprend l'algorithme précédent en "économisant" l'affectation de la ligne 6, on obtient ceci :
```PSEUDOCODE
	VARIABLES
	tab : tableau de longueur n
	e : entier
	DEBUT
		i <- 1
		TANT QUE i<=longueur de n :
			SI tab[i]=e:
				RENVOYER VRAI
			SINON :
				i=i+1
			FIN SI
		FIN TANT QUE
		RENVOYER FAUX
	FIN
```

La fonction qui calcule la longueur d'un tableau en python est `len(tab)`. Cette fonction a une complexité de $2n+2$.  


```python
def taille(l):
    i = 0 #1 opération executée que une seule fois
    while True:
        try: #ces opérations seront répétées autant de fois qu'il y a d'éléments dans le tableau
            _ = l[i] #1 opération
            i += 1 #1 opération
        except IndexError:
            return i #1 opération executée que une seule fois
```

A chaque tour, on doit recalculer la longueur du tableau, on obtient donc $n\times(2n+2+3)+2$ soit, si on simplifie $2n^2+5n+2$. 

!!! success "Détail"
	on repète la boucle n fois.  
	A chaque tour on recalcule la longueur $2n+2$, on fait la comparaison du TANT QUE, celle du SI, l'incrémentation du i (3 opérations).  
	Il y a une affichection et un renvoi exécutés que une fois (+2).  

On note que ici le nombre d'étapes n'est plus proportionnel à n mais sous forme de polynôme. On simplifie en disant qu'elle est proportionnelle à $n^2$, on dit que la complexité est **quadratique** et on l'écrit : **$O(n^2)$**  

## Algorithmes de tris
### Tri par selection 
Voici le pseudo-code du tri par sélection. Le *pire des cas* dans le cas d'un tri est d'avoir à trier das l'ordre croissant un tableau préalablement dans l'ordre décroissant.

```PSEUDOCODE
	VARIABLES
	t : tableau de longeur n
	DEBUT
      n ← longueur(t) 
      pour i de 0 à n - 2
        |  min ← i       
        |  pour j de i + 1 à n - 1
        |   |   si t[j] < t[min]
        |   |    | min ← j
        |   |   fin si
        |  fin pour
        |  si min ≠ i
        |  	| échanger t[i] et t[min] # un échange correspond à 3 opérations
        |  fin si
      fin pour
  	FIN
```
Dérouler l'algorithme **à la main** et chercher à exprimer la complexité.

!!! question "Complexité du tri par sélection"
	<form id="test1">
		<label><input type="radio" name="test" value="A"> linéaire</label><br>
		<label><input type="radio" name="test" value="B">quadratique</label><br>
	    <input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" id="BoutonValider" id="bouton" type="button" onclick="reactionQCU1()" value="Vérifier">  <input id="bouAffQCU1" type="button" onclick="AfficheQCU1()" value="Correction" style="display:none;"><br><br>
	</form>
         <div  style="font-weight: bold;" id="messageQCU1"></div>
         <div id="correctionQCU1" style="display:none;"> <p> Allez voir en dessous...</p></div>

??? tip "Une petite aide?"
	Opération exécutée une seule fois : ligne 4  
	On répète (n-1) fois les lignes 5,6 12 et 13 (soit 5 opérations), mais aussi les lignes 7 à 9 (n-1) fois  
	Soit : $1+(n-1)\times(5+(n-1)\times3)$  
	On développe et on simplifie : $3n^2-n-1$

Exécuter ce code pour vérifier  

<iframe width="100%" height="500" frameborder="0" src="https://console.basthon.fr/?script=eJydUkFuwjAQvEfKH1biQKJCFa6Vwhs49IYiZJKFLopjy7Er-iTewce6XiApRVXV-mDZs-uZ8dikrXEePGlMkzSZwMqZvVNaI6w-_JvpwJrgoJ2Stu35pLHzyhPDTQDvCKxy0GOLdQTTpMFdhDcDlHm1zV_SBAB2xgEBdeBUt8esxUvxWuUxgVdnwjuyHIKm7obHNZRAwz4yHUYmelrM4JFOBrEftV0zQwVLWR6q-45R4PCAw4B4bbkjnqdqBGV7xaPEXUU0y3hSYIc-uC5WvgdtHXU1WcW3lrA99v4SQm0anmjeYN-HPk38ZlEUBZOujxLCcQgBsliZFbP5Iq9ujUX5Q9_YyE6a4M4nhGaKR6yDPK7YCGK2RRWAXYjw-XT9A-yl94o_Tilf5zlOWc66928vLnJOMV7RZ19aYQ5CkP_Rwj89_GLiEypq6Lw"> </iframe>

### Tri par insertion

```PSEUDOCODE
	VARIABLES  
	t : tableau de longeur n  
	DEBUT 
      n ← longueur(t)   
      POUR i de 1 à n - 1  
        |  x ←t[i]  
        |  j ← i     
        |  TANT QUE j > 0 et t[j - 1] > x  
        |   |   T[j] ← T[j - 1]  
        |   |   j ← j - 1  
        |  FIN TANT QUE    
        |  t[j] ← x  
      fin POUR  
  	FIN  
```
Dérouler l'algorithme **à la main** et chercher à exprimer la complexité.
!!! question "Complexité du tri par insertion"
	<form id="test2">
		<label><input type="radio" name="test" value="A"> quadratique</label><br>
		<label><input type="radio" name="test" value="B">linaire</label><br>
	    <input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" id="BoutonValider" id="bouton" type="button" onclick="reactionQCU2()" value="Vérifier">  <input id="bouAffQCU2" type="button" onclick="AfficheQCU2()" value="Correction" style="display:none;"><br><br>
	</form>
         <div  style="font-weight: bold;" id="messageQCU2"></div>
         <div id="correctionQCU2" style="display:none;"> <p> Allez voir en dessous...</p></div>

Exécuter ce code pour vérifier  

<iframe width="100%" height="500" frameborder="0" src="https://console.basthon.fr/?script=eJydkk1ugzAQhfdI3OFJXQTUUMG2KjlD9hGKHJgkJsYgY9T0Nt3mHFysY-ePSK2q1gsWzzPfPN5YNl1rLKxsKAzC4AlL0-6MaBrC8sPuW42uHQzUTDadGk8NaSusZLkaYI1EJwyk7sk4MQwq2jp5fZMiKzbxK8IAfJguTOl4FSHD-AklYIVUijxPbM5125ahjIURekdRNoeiM-mGcueA3PWsZDERaxZlkt2F971kfI1FjhRCV9z25tvqAlPa9fgrPCMrLvi6-KaqRpJjMuWh6-CifAyzM1KXshNsxQdqqbfEuRLKlsMoZVJR3w99GNh1lqYpU1ZHH8TxFgQidzNP50kWF9fCNP-h7l7ITqrBjCcOeUZHKge_QG9j0M65IjH4lbjB4-myZ_bSW8GPI_fP48V9opjnPu7Xu4g5IveLNpqUIoEHxH-08E8Pv5j4AnvJ3nQ"> </iframe>


??? tip "Une petite aide?"
	Opération exécutée une seule fois : ligne 4  
	On répète (n-1) fois  : 5,6,7 et 12 (4 opérations) et (n-1) fois max les lignes 8,9,10 (5opérations)
	Soit $1+(n-1)\times(4+(n-1)\times5)$ si on simplifie, on trouve $5n^2-n-2$  

!!! fail " Pour faire court"
	**De manière générale**, un programme qui contient une boucle POUR ou TANT QUE a une complexité linéaire. Lorsque l'on a des boucles imbriquées, dans le pire des cas, la complexité sera quadratique.  
	Il faudra cependant être vigilant aux opérations cachées lorsque l'on utilise des méthodes de listes comme `len()`, `sum()`, `min()` ou `max()` par exemple.


## Recherche dicothomique
Nous allons comparer l'éxécution d'une recherche classique et d'une recherche dicothomique :

Ecrire une fonction python (dans Thonny) qui recherche `3` dans un tableau de 100000 éléments que nous allons créer par cette ligne `tab=[x for x in range (100003,2,-1)]`.
Ecrire (ou copier du TP précédent) le programme de recherche dicothomique et mesurer le temps d'éxécution des deux fonctions (en utilisanst les exemples vus précédement pour les tris.)  
Multiplier ensuite par 10 la taille du tableau puis afficher à nouveau les résultats. 


!!! success "Evolution"
	La complexité de la recherche dicothomique semble être linéaire. Il faudrait l'essayer avec de très grands tableaux pour se rendre compte qu'elle est en ait logarithmique **$O(log(n))$**. C'est à dire que pour des tableaux très grands elle sera plus efficace qu'une recherche linaire. C'est souvent le cas lorsque l'algorithme diminue la zone de recherche à chaque étape.

## Visualisation graphique
Sur le graphique ci-dessous vous pouvez voir comment évolue la complexité en focntion de la taille des données à traiter. Sur un petit problème, ela n'aura pas d'importance, mais la différence peut être énorme sur le traitement d'un grand nombre de données. D'où l'interet de chercher toujours à diminuer la complexité de son programme en choisissant l'algorithme adapté et en vérifiant que l'on ne fait pas de caluls inutiles ou redondants.

![evolution des complexités en focntion de la taille du tableau](https://dlatreyte.github.io/premieres-nsi/chap-16/fig-16-2.png)

## Comparaison des différents tris

Sur cete animation, on peut voir la vitesse de réalisation de tris de tableaux en fonction de l'algorithme utilisé et de la façon dont le tableau est rangé au départ.

![gif tris](img/comparaisons.gif)

On retrouve les tris par insertion et selection, le tri à bulle, le tri de Shell, le tri fusion (Merge), le tri par tas (Heap) et deux sortes de tris rapides.  
Les tableaux de départs sont (dans l'ordre) : aléatoire, presque trié, dans l'ordre inverse du tri que l'on souhaite (pire des cas), cas de valeurs non uniques.
<!---Javascript-->
<script>
function reactionText1(){
	var msg;
	var reponse=document.getElementById("reponse1");
	if (reponse.value ==='40'){
		msg='bravo';
		style='style="color:green;"';
		}
	else{msg='non, essaye encore';
	style='style="color:red;"';}
	document.getElementById("messageText1").innerHTML='<p '+style+'>'+msg+'</p>';
	document.getElementById("bouAffText1").style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;display:inline;";
}

function AfficheText1(){
	document.getElementById("correctionText1").style="display:block;";
}

function reactionText2(){
	var msg;
	var reponse=document.getElementById("reponse2");
	if (reponse.value ==='2n' || reponse.value ==='2*n'){
		msg='bravo';
		style='style="color:green;"';
		}
	else{msg='non, essaye encore';
	style='style="color:red;"';}
		document.getElementById("messageText2").innerHTML='<p '+style+'>'+msg+'</p>';
		document.getElementById("bouAffText2").style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;display:inline;";
}

function AfficheText2(){
	document.getElementById("correctionText2").style="display:block;";
}

function reactionText3(){
	var msg;
	var reponse=document.getElementById("reponse3");
	if (reponse.value ==='3n+3'){
		msg='bravo';
		style='style="color:green;"';
		}
	else{msg='non, essaye encore';
	style='style="color:red;"';}
		document.getElementById("messageText3").innerHTML='<p '+style+'>'+msg+'</p>';
		document.getElementById("bouAffText3").style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;display:inline;";
}

function AfficheText3(){
	document.getElementById("correctionText3").style="display:block;";
}

function reactionQCU1(){
	var style;
	var msg;
	var reponse = document.getElementById("test1");
	var rep=reponse.elements["test"].value;
	console.log(rep);
	if (rep=="B"){msg='bonne réponse';
	style='style="color:green;"';
	}
	else {msg='mauvaise reponse';
	style='style="color:red;"';}
	document.getElementById("messageQCU1").innerHTML='<p '+style+'>'+msg+'</p>';
	document.getElementById("bouAffQCU1").style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;display:inline;";
}
/*affiche la réponse si on clique sur le bouton correction*/
function AfficheQCU1(){
	document.getElementById("correctionQCU1").style="display:block;";
}

function reactionQCU2(){
	var style;
	var msg;
	var reponse = document.getElementById("test2");
	var rep=reponse.elements["test"].value;
	console.log(rep);
	if (rep=="A"){msg='bonne réponse';
	style='style="color:green;"';
	}
	else {msg='mauvaise reponse';
	style='style="color:red;"';}
	document.getElementById("messageQCU2").innerHTML='<p '+style+'>'+msg+'</p>';
	document.getElementById("bouAffQCU2").style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;display:inline;";
}
/*affiche la réponse si on clique sur le bouton correction*/
function AfficheQCU2(){
	document.getElementById("correctionQCU2").style="display:block;";
}

</script>