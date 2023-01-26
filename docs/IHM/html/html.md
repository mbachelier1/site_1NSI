#Bases du langage `HTML`
##Introduction
Le langage html est interprété par les navigateurs internet. Il repose sur la norme W3C. 
C'est un langage qui utilise des balises pour la mise en forme d'un texte. 
Exemple pour écrire du texte en gras on utilise la balise "strong" 
Chaque balise est écrite ente les symboles < et >, et doit être refermée (symbole /). 
(Certaines sont auto-fermantes comme `<br/>`, `<img/>`, `<meta/>`).  

!!! example "Par exemple :"
    ```html
    blablabla<strong>youpi</strong>blablabla, va écrire" youpi" en gras.
    ```

Toute page commence par `<!DOCTYPE html >` et finit par `</html>`.

Ensuite il y a l'entête qui contient divers renseignements importants : le titre de la page ,balise `<title>`,

- le nom de l'auteur, (facultatif)
- le mode d'encodage, (TRES IMPORTANT)
- le lien vers la feuille de style (voir chapitre suivant), …..balises auto fermante `<meta>`
- les mots clés qui favorisent le référencement de votre site par les moteurs de recherche

Elle est délimitée par les balises `<head>` et` </head>` 

!!! example "Voici un exemple :"
    ```html
    <head> 
        <title> Page Web de la spécialité NSI </title> 
        <meta name="author" content="Cligniez-Djebali" /> 
        <meta charset = "utf-8" />  
        <meta NAME="keywords" CONTENT="mot1,mot2, mot3"/> 
    </head>
    ```



!!! important "Important"
    On a souvent des problèmes d'accents avec les pages WEB, les bases de données, … C'est pourquoi il faut prendre garde au mode d'encodage des caractères. Je vous recommande d'utiliser le jeu de caractères UTF-8. Mais attention, votre fichier doit lui aussi être encodé en UTF-8! Dans l’éditeur de texte dans l'onglet "encodage", choisissez "Encoder en UTF8 (sans BOM)".

Puis vient le corps de la page " body " entre les balises `< body>` et `< /body>` C'est entre ces balises que se trouvent les éléments de votre page. 

##Premières balises `HTML`
Il y a 6 balises de titres : h1, h2, h3, ….(ordre décroissant de taille) Les textes sont écrits entre les balises de paragraphes `<p>` et `</p>` Un saut à la ligne est provoqué par la balise auto fermante`.  `

`<strong>` et `</strong>` permettent d'écrire en gras, `<em>` et `</em>` en italique, `<sub>` et `</sub>` en indice `<sup>` et <`/sup>` en exposant.
Voici donc une première page web :  
Pour l’écrire on utilise un simple éditeur de texte (par exemple sublime text, ou notepad++ qui pratique une coloration syntaxique bien pratique.)
Il est plus lisible pour la présentation, d'utiliser l'indentation comme en python. Ainsi on risque moins de se tromper dans les balises imbriquées.  

!!! important "Fichier à créér"
    ```html
    <!DOCTYPE html > 

    <head> 
      <title> Page test de la spécialité NSI </title> 
      <meta charset ="utf-8" /> 
                  <meta NAME="keywords" CONTENT="mot1,mot2, mot3"> 

    </head> 

    <body> 
      <h1>Voici un gros titre</h1> 
      <p>Le langage xhtml permet d'écrire des textes <strong>en gras</strong> ou  
      <em>en italique</em>. On peut passer à la ligne,<br/> 
      et écrire des exposants ou des indices : u<sub>n</sub>=n<sup>2</sup>+1.</p> 
    </body> 

    </html>
    
    ```

Enregistrer ce fichier sous le nom **" test.html "** et ouvrez avec un navigateur. 
La page est très dépouillée ! On apprendra plus tard à mettre des couleurs, des bordures, des logos avec les feuilles de style et le langage 
`CSS`.



##Les liens
L’intérêt essentiel des pages web est l'utilisation des liens. Les balises sont `<a>` et `</a>`.  
!!! info "Un lien peut être absolu : "
    ```html
    <a href="http://www.google.fr">Moteur de recherche</a>
    ```
    affiche " Moteur de recherche " et lorsqu'on clique dessus, envoie sur [www.google.fr](www.google.fr); 

!!! info "Un lien peut être relatif : "
    ```html
    <a href="python.html">Ma page de programmation</a>
    ```
    affiche " Ma page de programmation " et lorsqu'on clique dessus envoie sur la page python.html qui doit être dans le même dossier que la page qui contient le lien.     

On peut changer de dossier en écrivant par exemple: 
!!! example "exemple"
    ```html
    <a href="documents/python.html"> 
    ```

On peut aussi faire un lien vers un autre endroit de la même page (utile pour un lexique par exemple). Il faut d'abord créer une "ancre" à l'endroit que l'on veut atteindre par le lien, avec: 

!!! method "creer une ancre"
    Créer une ancre
    ```html
    <a name="toto">On veut aller ici</a>    
    ```
    Puis créer le lien avec : 
    ```html
    <a href="ma_page.html#toto">
    ```


##Les listes 
On dispose de 2 types de listes. Les listes à puces délimitées par les balises `<ul>` et `</ul>` et les listes numérotées délimitées par `<ol>` et `</ol>`. Chaque élément de la liste est alors délimité par `<li>` et `</li>` :

!!! method "Créer une liste"
    ```html
    <ul >Voici une liste de choses :
        <li> 1er élément </li>
        <li> 2eme élément </li>
        <li> 3eme élément </li>
    </ul>
    ```

##les images
On insère une image par la balise auto-fermante : 
!!! example "exemple"
    ```html
    <img src="images/mon_image.jpg" />    
    ```
ce qui affiche l'image "mon_image.jpg" situé dans le dossier "images" qu’il faut créer.

ou si l'image est ailleurs, avec son adresse absolue : 
!!! example "exemple"
    ```html
    <img src=" https://i2.wp.com/beebom.com/wp-content/uploads/2016/01/Reverse-Image-Search-Engines-Apps-And-Its-Uses-2016.jpg?w=640&ssl=1 " />    
    ```
 Il est souhaitable (indispensable pour respecter W3C) d'ajouter un texte alternatif, en cas de problème de chargement, pour les non-voyants, …  

 !!! example "exemple"
    ```html
    <img src="robot.jpg" alt="photo du robot Thymio 2"/>    
    ```
##Les tableaux
On peut insérer un tableau par les balises. `<tr>` est la balise de ligne, `<td>` est la balise de cellule. 

!!! method 'Créer un tableau'
    ```html
    <table>
        <thead>
            <tr>
                <th>1ere colone</th>
                <th>2eme colonne</th>
                <th>3eme colonne</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> case 1 </td>
                <td> case 2 </td>
                <td> case 3</td>
            </tr>
            <tr>
              <td> case 4 </td>
              <td> case 5 </td>
              <td> case 6</td></tr> 
        </tbody>
    </table>
    ```
!!! caution "important"
    on peut fusionner des cellules notamment dans le `header` : 
    ```html
    <table>
        <thead>
            <tr>
                <th colspan="3">The table header</th>
            </tr>
            ...
    ```
##Exercice
Créer au moins 3 pages `html` (pour exploiter les liens!!)
La première sera nommée "index.html", page de base de votre site. Elle comportera un titre h1, au moins un paragraphe, des mots en gras, en italique.
Elle comportera aussi un lien vers une deuxième page nommée "page1.html" qui aura aussi un titre un paragraphe et un lien de retour vers votre page "index".
Compléter avec une troisième page, accessible par lien depuis la page "index", qui comportera une liste ( `<ul>`)de liens absolus vers des sites de votre choix.
Votre site doit contenir au moins un élément de chaque type vus précédememnt (listes, tableausx, images, ...).   

Commencez une fiche de référence des balises html essentielles. Vous rajouterez toutes celles rencontrées au cours du travail à réaliser dans les prochaines semaines. Réservez le dos de la fiche pour le mémo `CSS`.  

##Compléments
Le web fournit une très grande quantité de tutoriel sur le HTML. N'hésitez pas à aller voir toutes les balises existantes, notamment pour intégrer des vidéos ou d'autres istes web à votre site.   

En naviguant sur Internet, lorsque vous trouvez une belle présentation, faites un clic droit sur la page et choisissez "afficher la source", et vous obtenez le code xhtml.  
Attention, c'est parfois du lourd car il y a des codes javascript , du style css, mélangés au html. Mais ça donne des idées…..  

Une fois que votre site est testé en local sur votre PC, vous pouvez passer à l'étape suivante et le mettre en ligne en [jetant un oeil par ici](https://openclassrooms.com/fr/courses/918836-concevez-votre-site-web-avec-php-et-mysql/918167-envoyez-votre-site-sur-le-web).  