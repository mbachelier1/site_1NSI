#Programmation évènementielle
##Atteindre un élément de la page html
Tester ce code et n'oubliez pas d'aller voir dans la console.  

!!! faq "Question"
    Expliquer ce qu'il fait.

```html
<!DOCTYPE html>
<html>
  <head>
      <title>Réupérer un élément html</title>
      <meta charset="UTF-8" />
  </head>
  <body>
      <p id="1">voici un premier <strong>paragraphe</strong> dont l'identifiant est "1"</p>
      <p id="2">voici un autre paragraphe dont l'identifiant est "2"</p>
      <script>
        console.log(document.getElementById("1"));
        console.log(document.getElementsByTagName("p"));
      </script>
  </body>
</html>
```

!!! faq "Questions"
    **1.** Identifier ce que fait le code javascript en consultant la console.  
		**2.** Expliquer à quoi servent les commandes `document.getElementById` et `document.getElementsByTagName`. 
		**3.** Ajouter `.innerHTML` à la suite de `document.getElementById`. Que récupère la commande ?  
		**4.** Même question en remplaçant `innerHTML` par `innerText`. 

##Manipuler le html :
```html
<script>
      document.getElementById("1").innerHTML = "je modifie mon paragraphe";
</script>
```
!!! faq "Questions"
    **5.** Remplacer "=" par "+=". Que se passe-t-il?
    **6.** Que fait ce code? Le tester.

```html
  <body>
    <a id="myLink" href="http://www.google.com">
      Un lien modifié dynamiquement
    </a>
    <script>
      var link = document.getElementById("myLink");
      var href = link.getAttribute("href"); // On récupère l'attribut « href »
      alert(href);
      link.setAttribute("href", "https://informatiquelha.wordpress.com/");
      // On édite l'attribut « href »
    </script>
  </body>
```

!!! faq "Questions"
    **7.** Modifier le code de façon à créer un lien vers le site informatiquelha.wordpress.com dans le deuxième paragraphe. Ce lien doit avoir un identifiant `id`.

##Manipuler le `css`
```html
<html>
  <head>
    <title>Parcel Sandbox</title>
    <meta charset="UTF-8" />
    <style>
      #exemple {
        background-color: #ff0;
        color: #0f0;
        font-size: 1.2em;
        text-align: center;
      }
    </style>
  </head>

  <body>
    <div id="exemple">Pif paf pouf</div>
    <script>
      // on récupère l'élément
      var elmt = document.getElementById("exemple");
      alert("on récupère l'élément exemple et on en modifie le style");
      // on modifie son style
      elmt.style.backgroundColor = "gray";
      ...
    </script>
  </body>
</html>
```

!!! faq "Questions"
    **8.** Etudier ce code et le compléter de façon à ce que le texte s'écrive en noir, aligné à droite et d'une hauteur de 1.8em.
    ??? note "Une petite aide?"
        Le JavaScript ne supporte pas les tirets. On remplacera donc background-color par backgroundColor.  

##Les évènements
###Evènements liés à la souris

Tester ce code et chercher les éléments qui déclenchent le changement.

<p class="codepen" data-height="350" data-theme-id="dark" data-default-tab="html,result" data-user="muriel722" data-slug-hash="xxZPJyx" style="height: 350px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="flash">
  <span>See the Pen <a href="https://codepen.io/muriel722/pen/xxZPJyx">
  flash</a> by muriel722 (<a href="https://codepen.io/muriel722">@muriel722</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>


!!! faq "Questions"
    **9.** L'évènement `mouseout` détecte le fait que la souris quitte la zone. Modifier le code pour que le paragraphe reprenne sa forme originale lorsque la souris quitte la zone.  

Voici ce que l'on peut faire d'autre :

<img src="../src/evt_souris.png" alt="évènements liés à la souris"></p>

###Evènements liés au clavier
Tester ceci :

!!! hint "Code"  

    === "html"
      ```html
      <!DOCTYPE html>
        <body>
          <p>Taper sur une touche</p>
          <p id="aremplir3"></p>
          <script src="index.js"></script>
        </body>
      ```

    === "javascript"
      ```js
      var texte0 = " ; elle correspond au caractère ";
      var zone3 = document.getElementById("aremplir3");
      var texte3 = "vous avez frappé la touche de code ";
      document.addEventListener("keypress", function(e) {
        zone3.innerHTML =
          texte3 + e.keyCode + texte0 + String.fromCharCode(e.keyCode);
      });
      ```


!!! faq "Questions"
    **10.** Que font les fonctions `keyCode` et `String.fromCharCode(e.keyCode)`?  
    **11.** Remplacer `keypress` par `keydown` puis `keyup`. Quelles sont les différences (notamment en terme d'affichage)?  






