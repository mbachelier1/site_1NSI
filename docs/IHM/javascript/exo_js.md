#Exercices d'application de `Javascript`
##Bac à sable
Pour faire des tests rapides sans enregistrer, on peut utiliser un "Bac à sable".

[Bac à sable](http://jsbin.com/wuqevezoku/edit?html,js,console){ .md-button }

##Utilisation de la console

Voici un code `html` contenant du `javascript`.

```html
<html>
  <head>
    <title>Ma Page avec un JS inclus</title>
      <script language="JavaScript">
        alert("JavaScript est maintenant inclus dans mon fichier et ce message s'affiche dans une fenêtre d'alerte");
      </script>
  </head>
<body>
    <p>Page avec JavaScript inclus dans mon code HTML</p>
</body>
</html>

```

!!! faq "A faire"
    **1.** Copier et tester ce code dans une page html que vous ouvrirez dans un navigateur.  
    **2.** Que fait la fonction `alert` ? 

Pour faire afficher les messages dans la console (F12 puis console), on utilise la fonction `console.log(a)` pour afficher la valeur de a par exmple. Cela evite la fenêtre popUp pour des vérifications en cours de code.  

!!! faq "A faire"  
    **3.** Modifier le code pour que le message s'affiche dans la console.  

##Variables et interaction utilisateur
###Syntaxe du Javascript

- Les variables doivent être déclarées grâce au mot clé var.  
- Tout comme en python, les chaînes de caractères sont entourées de guillemets.  
- Les instructions simples sont terminées par un point-virgule: ;   
- Les blocs d'instructions sont entourés d'accolades {}  
- Les commentaires sont notés précédés de deux barres obliques: //.  
- Les variables et fonctions sont écrites en camelCase(L'espace est remplacé par -une majuscule).  
- L'indentation des blocs d'instruction n'est pas obligatoire comme en Python, mais souhaitable pour plus de lisibilité du code.  

###Exemple
Tester ceci :  
```js
var tonNom ='Nom';
var tonPrenom ='Prenom';
var toi=tonNom+' '+tonPrenom;
alert(toi);
```

Puis ceci :  
```js
var tonNom =prompt('quel est ton nom?');
var tonPrenom =prompt('quel est ton prénom?');
var toi=tonNom+' '+tonPrenom;
if (tonNom=='Einstein'){  
  alert(toi+ ':tu est un génie!');}
else {
  alert(toi+ ':tu est juste un être humain');} 
```

##Fonctions et calcul :
Pour créer une fonction, on utilise la syntaxe ci-dessous :  
```js
function carre(nombre){
  return nombre*nombre
}
```
Pour exécuter la fonction :  
```js
var c
c=carre(4)
console.log(c)
```
!!! note "Remarque"
    La notion de porté de variable est valable aussi en Javascript. Pour déclarer une variable qui ne sera valable que dans un bloc ou une fonction on peut utiliser le mot-clé `let` au lieu de `var`. 


!!! faq "A faire"
    **4.** Ecrire une fonction qui calcule l'aire du disque dont le rayon est donné par l'utilisateur.
    ??? note "Une petite aide?"
          Il faudra commener par utiliser une fonction permettant de rentrer une valeur par l'utilisateur. Puis créer la fonction qui renvoie le calcul et enfin un affichage du résultat. (note : `Math.PI` permet d'obtenir la valeur de pi. ).

##Les boucles et les conditions
Pour chacune des syntaxes données ci-dessous, tester l'exemple donné et créer quelques lignes pour vous entrainer.  
Vous pouvez si vous êtes à l'aise tester les instructions proposées en dessous.  

###Syntaxe des conditions
```js
var result;
var a=-5
if (a>0) {
  result='positive';
} else {result='Not positive';}
console.log(result);
```
Plus d'exemples [par ici](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/if...else)  
Il existe aussi la fonction `SWITCH` dans le cas où il y a plusieurs conditions. Aller voir  [par ici](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/switch).  

###Syntaxe de la for
```js
var str='';
for (var i=0;i<9;i++){
  str=str+i
}
console.log(str);
```
`for ... in` et `for...of` peuvent être également utiles.  

###Syntaxe de la boucle while
```js
var n=0;
while (n<3){
  n++;
}
console.log(n);
```
Voir aussi `do...while`.  
D'autres instructions [ici](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements).  

###Applications
!!! faq "A faire"
    **5.** Ecrire un script en utilisant une boucle for qui demande à l'utilisateur le nombre de frères et soeurs qu'il possède. Puis le programme demande les prénoms de chacun.  
    **6.** Ecrire un script qui calcule l'altitude de chute d'un parachutiste à chaque seconde. On estime qu'il descend à une vitesse de 15m/s en partant de l'altitude de 1000m. On supposera qu'il s'arrete au sol.  
    **7.** Réaliser le script qui demande l'age de l'utilisateur et lui renvoie le commentaire correspondant.  


|Tranche d'âge|Commentaires|  
|:-----------:|:----------:|  
|de 1 à 17 ans|Vous n'êtes pas encore majeur|  
|de 18 à 49 ans|Vous êtes majeur mais pas sénior|  
|de 50 à 59 ans|Vous êtes sénior mais pas encore retraité|  
|De 60 à 120 ans|vous etes retraité profites de votre temps libre|  

##Où insérer le code `Javascript`?  
Cela dépend de ce dont vous avez besoin.  

**Pour une ou quelques lignes de code**  
Dans le code `html` entouré des balises `<script>` et `</script>` .  
```html
<html>
  <body>
    <h1>Ceci est ma super page</h1>
    <p>et voici un petit paragraphe pour occuper l'espace.</p>
    <script>
      alert("Bonjour tout le monde"); 
    </script>
    <p>et voici un autre paragraphe pour occuper l'espace.</p>
  </body>
</html>
```
ou  
```html
 <body>
    <h1>
      Ceci est une page de test de javascript
    </h1>
  <p>et voici un petit paragraphe pour occuper l'espace.</p>

    <script type="text/javascript">
      var a = 1;
      if (a == 1) {
        alert("ceci est n'importe quoi");
      } else {
        alert("c'est mieux");
      }
    </script>
  </body>
```

**Pour un code plus long**  
On crée un fichier `.js` séparé et on y fait référence dans le code `html` .

```html
 <script type="text/javascript" src="monfichier.js"></script>
```

Il peut même y avoir plusieurs fichiers `.js` attaché à une page `html`.  

##Mise en place du code PROPREMENT 
Créer trois fichier dans votre éditeur de texte et séparer les codes `html`, `css` et `javascript` du premier exercice puis vérifier que tout fonctionne.



