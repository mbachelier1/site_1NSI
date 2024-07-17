# Programmer en Javascript
On utilisera la console JS de basthon. N'oubliez pas de télécharger le programme une fois terminé.

[Bac à sable](http://jsbin.com/wuqevezoku/edit?html,js,console){ .md-button }
Ne garder que les onglets javascript et console pour l'instant.

Voici quelques règles que vous devez connaître avant de commencer :

!!! tip "Règles de base"
	
	- Les variables doivent être déclarées grâce au mot clé `var` ou `let`.  
	- Tout comme en python, les chaînes de caractères sont entourées de guillemets.  
	- Les instructions simples sont terminées par un point-virgule: ;   
	- Les blocs d'instructions sont entourés d'accolades {}  
	- Les commentaires sont notés précédés de deux barres obliques: //.  
	- Les variables et fonctions sont écrites en camelCase(L'espace est remplacé par une majuscule).  
	- L'indentation des blocs d'instruction n'est pas obligatoire comme en Python, mais souhaitable pour plus de lisibilité du code.  


## Déclarer les variables
Javascript est un langage faiblement typé. Cela signifie que lorsqu'on déclare une variable, il n'est pas nécessaire de déclarer son type. Il suffit de déclarer son **nom**, en ajoutant devant les mots-clés let ou var selon la situation2. On peut aussi **déclarer et initialiser** une variable dans le même temps :  
```JS
let x ; // x est déclarée, mais pas initialisée
let y = 10; // y est déclarée et initialisée à la valeur 10

var z ="toto";  // z est déclarée et initialisée avec la chaîne "toto"
```
Sachez seulement que :  
- `let` définit des variables dont la portée (=l'ensemble des lignes où la variable est connue et utilisable) est celle du bloc ;  
- `var` définit des variables dont la portée est celle de la fonction.  
Pour ceux intéressés les exemples ci-dessous sont parlants  

!!! example "Exemples"
	les deux codes suivant expliquent en partie la différence entre `let` et `var` :
	```JS
	    function varTest() {
	    var x = 31;
	    if (true) {
	    var x = 71;  // c'est la même variable (même fonction)!
	    console.log(x);  // 71
	    }
	    console.log(x);  // 71
	    }

	    function letTest() {
	    let x = 31;
	    if (true) {
	    let x = 71;  // c'est une variable différente (changement de bloc)
	    console.log(x);  // 71
	    }
	    console.log(x);  // 31
	    }
	```  
## Récuparétion et affichage des données

!!! succes "Tester ceci"  
	```js
	var tonNom =prompt('quel est ton nom?');
	var tonPrenom =prompt('quel est ton prénom?');
	var toi=tonNom+' '+tonPrenom;
	console.log(toi);
	```

La commande `prompt()` sert à interagir avec l'utilisateur par une fenêtre popup en lui demandant de remplir un champ.  

!!! question "Remplacement"
	**1** Remplacer `console.log` par `alert`.  
	**2** Quelle est la différence entre les deux?  

!!! note "Utilisation"
	De manière générale, lorsque l'on code on utilisera plutôt la commande `console.log` mais lors de l'interaction avec l'utilisateur, on utilisera plutôt la commande `alert`. En effet, celui-ci n'est pas censé avoir besoin de la conole. 


## Chaines de caractères
Le type primitif chaîne de caractère en javascript est repéré comme en python par un encadrement par des guillemets simples ', doubles " ou même des accents graves `.  

Ce type primitif est converti automatiquement en objets `String` dès qu'on fait appel aux méthodes des objets `String`. Ainsi si ma_chaine est une chaine de caractère :   

`ma_chaine.length` donne la longueur de la chaîne de caractères ;  
`ma_chaine.toLowerCase()` renvoie la chaîne de caractères en minuscules ( n a de même `.toUpperCase()`)  
`ma_chaine[i]` renvoie le caractère d'indice i (toujours en partant de zéro !)  
...
La totalité des méthodes liées aux objets `String` sont décrits dans [cette page](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/String#m%C3%A9thodes_des_instances).  

!!! danger "Javascript et transtypage"
	En Python, une instruction telle que `"Bonjour numéro "+6` ne fonctionne pas. On reçoit une erreur `TypeError: can only concatenate str (not "int") to str`, ce qui signifie qu'il est impossible de concaténer un type `str` avec autre chose. Contrairement à Python, en javascript il n'est pas nécessaire de transtyper une variable pour qu'elle soit intégrée à une opération avec d'autre types de variables. L'instruction `"Bonjour numéro "+6` renvoie la chaîne de caractères `"Bonjour numéro 6"`.  
	C'est très pratique, mais attention ! Certaines erreurs peuvent très vite être commise ! Un petit exemple de comportement de Javascript est donné dans l'exemple ci-dessous :
	<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=let%20a%20%3D%20'5'%20-%203%3B%0Alet%20b%20%3D%20'5'%20%2B%203%3B%0Alet%20c%20%3D%20'5'-%20'4'%3B%0Alet%20d%20%3D%20'5'%20%2B%20%2B'5'%3B%0Alet%20e%20%3D%20'toto'%20%2B%20%2B%20'tata'%3B%0Alet%20f%20%3D%20'5'%20%2B%20-%20'2'%3B%0A%0Alet%20x%20%3D%203%0Alet%20y%20%3D%20'5'%20%2B%20x%20-%20x%3B%0Alet%20z%20%3D%20'5'%20-%20x%20%2B%20x%3B&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=js&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

## Fonctions et calcul :
Pour créer une fonction, on utilise la syntaxe ci-dessous :  
```js
function carre(nombre){
  return nombre*nombre
};
```
Pour exécuter la fonction :  
```js
var c;
c=carre(4);
console.log(c);
```
!!! question  "A faire"
    **3.** Ecrire une fonction qui calcule l'aire du disque dont le rayon est donné par l'utilisateur.
    ??? note "Une petite aide?"
          Il faudra commener par utiliser une fonction permettant de rentrer une valeur par l'utilisateur. Puis créer la fonction qui renvoie le calcul et enfin un affichage du résultat. (note : `Math.PI` permet d'obtenir la valeur de pi. ).

## Structures conditionnelles
La syntaxe générale est la suivante :
```JS
if ( booleen ){
    // Bloc Si
}
else {
    // Bloc Sinon
}

```

!!! example Exemple
	```js
	var result;
	var a=-5;
	if (a>0) {
	  result='positive';
	} else {result='Not positive';}
	console.log(result);
	```
	Plus d'exemples [par ici](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/if...else)  
	
!!! info "Remarques"
	- la condition booléenne doit être entre parenthèses. L'interpréteur javascript signalera une erreur dans le cas contraire.
	- il n'y a pas comme en Python de clause `elif`. Si on veut tester plusieurs sous conditions, il faudra imbriquer les structures conditionnelles. Voici une comparaison entre python et javascript :  
	=== "python"

		```python
		if condition 1 :
			# bloc condition 1
		elif condition 2 :
		    # bloc condition 2
		else :
		    # bloc sinon    
		```

	=== "Javascript"

		```JS
		if (condition 1){
		    // bloc condition 1
		}
		else {
		    if (condition 2) {
		        // bloc condition 2
		    } 
		    else {
		            // bloc sinon
		    }
		}
		```
	L'imbrication est tout de suite plus compliquée... Il faut être rigoureux, et particulièrement être attentif à bien fermer les accolades dès qu'on en a ouvert une.
	Il existe aussi la fonction `SWITCH` dans le cas où il y a plusieurs conditions. Aller voir  [par ici](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/switch).  

		

!!! danger "ET et OU en Javascript"
	Attention ! En javascript les mots-clés `AND `et `OR` n'existent pas :  
	- pour obtenir `ET` on utilise `&&`  ;  
	- pour obtenir `OU` on utilise `||` ;  

## Boucles Bornées (boucle `FOR`)
Une boucle bornée en javascript s'écrit de la manière suivante :
```JS
for (initialisation; conditions de continuité; incrémentation){
    // bloc d'instructions à répéter
}
```
Plus simplement, pour répéter 10 fois un bloc d'instructions, on peut utiliser la structure suivante :
```JS
for (let i=0; i<10; i=i+1){
    // bloc d'instructions à répéter
}
```

On commence par créer une variable sur laquelle on va itérer : `var i=0`;  
on indique une condition de continuité de l'action : `i<10`; (tant que i est inférieur à 10, on effectue le bloc d'instruction de la boucle)  
on indique comment varie la variable à chaque tour de boucle :` i=i+1 `(à chaque tour, la variable i est incrémentée de 1.  
Il faut noter que la variable i n'existe plus une fois la boucle terminée, vu qu'n a utilisé `let `:   
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=for%20%28let%20i%3D0%3B%20i%3C5%3B%20i%3Di%2B1%29%7B%0A%20%20console.log%28i%29%3B%0A%7D%0Alet%20k%20%3D%203*i%3B&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=js&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

## Boucles non bornées (Boucle `While`)
Une boucle non-bornée est obtenue en javascript par l'instruction suivante :
```JS
while (booleen) {
   // bloc d'instruction
  }
```
Un exemple d'utilisation avec les chaines de caractères est disponible ici :
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=let%20mot%20%3D%20%22toto%22%3B%0Awhile%20%28mot.length%3C50%29%20%7B%0A%20%20mot%20%2B%3D%20mot%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=js&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

## Applications
!!! question "A faire"
    **4.** Ecrire un script en utilisant une boucle for qui demande à l'utilisateur le nombre de frères et soeurs qu'il possède. Puis le programme demande les prénoms de chacun.  
    **5.** Ecrire un script qui calcule l'altitude de chute d'un parachutiste à chaque seconde. On estime qu'il descend à une vitesse de 15m/s en partant de l'altitude de 1000m. On supposera qu'il s'arrete au sol.  
    **6.** Réaliser le script qui demande l'age de l'utilisateur et lui renvoie le commentaire correspondant.  

	|Tranche d'âge|Commentaires|  
	|:-----------:|:----------:|  
	|de 1 à 17 ans|Vous n'êtes pas encore majeur|  
	|de 18 à 49 ans|Vous êtes majeur mais pas sénior|  
	|de 50 à 59 ans|Vous êtes sénior mais pas encore retraité|  
	|De 60 à 120 ans|vous etes retraité profitez de votre temps libre|  


