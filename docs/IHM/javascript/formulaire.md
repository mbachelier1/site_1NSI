# Créer un formulaire et récupérer les données

## Ajouter un élément au DOM

<iframe src="//video.toutatice.fr/video_priv/12995/116d0ebae718159b4ba0ab8c7758c3f8835e6611d3a35f9c9c6e31adb174b607/?is_iframe=true&size=240" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

## Construire un formulaire
<iframe src="//video.toutatice.fr/video_priv/12999/89ba09f9b0fdc5393d8e22f76d027477b6dc0c8719f4d5d14b4d6dd257d59d67/?is_iframe=true&size=240" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

## Récupérer les données du formulaire
<iframe src="//video.toutatice.fr/video_priv/13001/6b3469a9e2639fc6bf5edc485dd0ed3e94bc2b1226f4bdef9cea9f430c70e3f3/?is_iframe=true&size=240" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

## Rendre la page dynamique
<iframe src="//video.toutatice.fr/video_priv/13009/6f60c09c94597518a1f8f261d853f9f800eda07a23b025f194a2e16be72c7daa/?is_iframe=true&size=240" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

## Les différents élements de formulaires
!!! warning "Avant de commencer"
	De la même façon que le nom de vos variables doivent être explicites, veillez à choisir des noms d'identifiants et de classe compréhensibles et cohérents. Par exemple, si vous créez une liste déroulante pour demander l'âge d'une personne, ne l'appelez pas "liste" ou "listeDéroulante" mais "age".

### Le bouton

!!! example "Exemple"

	<form>
		 <input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;"  value="tester" onclick="testBidon()">
	
	</form>
	<div id="casecouleur"> Un élément de formulaire fondamental : le bouton</div>

!!! success "Code"

	=== "html"

		Le `input` créé un bouton qui exécute la fonction JS `ActionDuBouton()` lorsque l'on clique dessus. On crée en dessous un bloc `div` contenant du texte.   
		```html
		<form>
			<input type="button" value="tester"  onclick="ActionDuBouton()">
		</form>
		<div id="casecouleur"> Texte à colorer</div>
		```

	=== "javascript"

		Ici, on définit la fonction `ActionDuBouton()` qui change la couleur de fond (`backgroundColor`) du bloc dont l'`id` est `casecouleur`.
		```JS
		function ActionDuBouton(){
    				document.querySelector("#casecouleur").style.backgroundColor='aqua';
    		}
		```

### Boutons radio

!!! danger "Attention"
	Il faut donner le même nom (`name`) aux boutons radios mais des `id` différents

!!! example "Exemple"

	<form>
	    <label>1</label><input type="radio" name="testRad" value="1" id="radio1">
		<label>2</label><input type="radio" name="testRad" value="2" id="radio2">
		<label>3</label><input type="radio" name="testRad" value="3" id="radio3">
		<label>4</label><input type="radio" name="testRad" value="4" id="radio4">
		<input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" value="tester" onclick="testRadio()">
	</form>
		<div id="texteRadio" ></div>

!!! success "Code"

	=== "html"
		```html
			<form>
				   <label>1</label<input type="radio" name="testRad" value="1" id="radio1">
				   <label>2</label<input type="radio" name="testRad" value="2" id="radio2">
			 	 ...
			 	 <div id="texteRadio"></div>
				<input type="button" value="tester" onclick="testRadio()"> 
			</form>
		```

	=== "javascript"
		```js
		function testRadio(){
			var TexteTexteAEcrire="Le bouton radio sélectionné est le "; 
			if (document.querySelector('#radio1').checked) TexteTexteAEcrire+=1;
			if (document.querySelector('#radio2').checked) TexteTexteAEcrire+=2;
			if (document.querySelector('#radio3').checked) TexteTexteAEcrire+=3;
			if (document.querySelector('#radio4').checked) TexteTexteAEcrire+=4;
			document.querySelector('#texteRadio').textContent=TexteTexteAEcrire;
			}
		```
On crée une variable `TexteTexteAEcrire` avec le début de la phrase et on la complète par le numéro en fonction du bouton sélectionné.  
Le contenu de la variable `TexteTexteAEcrire` est affiché dans une balise `<div>` dont l'`id` est `texteRadio` initialement vide.

!!! question  "A faire"
	Compléter et tester le code pour ajouter les deux boutons radio manquant.


### Cases à cocher

!!! example "Exemple"

	<form>
	<div id="casesACocher">
		<input type="checkbox" name="testCase" value="Case 1" id="case1"><label>Case 1</label>  <br>  
		<input type="checkbox" name="testCase" value="Case 2" id="case2"> <label>Case 2</label>  <br>  
		<input type="checkbox" name="testCase" value="Case 3" id="case3"><label>Case 3</label><br>
		<input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" value="tester" onclick="testCases()">
	<div id="texteCases" ></div>
	</div>
	</form>


!!! success "Code"

	=== "html"
		```html
			<form>
				<div id="casesACocher">
					<input type="checkbox" name="testCase" value="Case 1" id="case1"><label>Case 1</label>  <br>  		  
					<input type="button" value="tester" onclick="...">
					<div></div>
				</div>
			</form>
			...
		```


	=== "javascript"
		```js
		function testCases(){
			var TexteAEcrire="vous avez coché ";
			if (document.querySelector('#case1').checked) TexteAEcrire+=" la case 1, ";
			if (document.querySelector('#case2').checked) TexteAEcrire+=" la case 2, ";
			if (document.querySelector('#case3').checked) TexteAEcrire+=" la case 3, ";
			document.querySelector('#texteCases').textContent=TexteAEcrire;
			}
		```

!!! question "A faire"
	Compléter le code HTML pour ajouter les deux cases manquantes, le bouton de validation et le bloc pour afficher le résultat dans un bloc en dessous du formulaire. 

!!! note "Remarques"

 	=== "Remarque 1"  
 		Ici le choix a été de faire apparaître la légende (Case 1) après le bouton donc après la balise.  
 
 	=== "Remarque 2"
 		Il faut donner le même nom (`name`) aux cases à cocher mais des `id` différents.  

### Liste déroulante

!!! example "Exemple"

	<form>
	<div id="MenuDeroulant">
	<select>
		<option name="selection" value="..." id="rien">....</option>
		<option name="selection" value="mot 1" id="mot1">mot 1</option>
		<option name="selection" value="mot 2" id="mot2">mot 2</option>
	</select>
	<input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" value="tester" onclick="testMenu()">
	</div>
	</form>
	<div id="texteMenu" class="rajout"></div>

on teste quel mot a été sélectionné `selected` ; on rajoute alors ce mot dans le texte (TexteAEcrire) à afficher dans le bloc d'identifiant "texteMenu".  

!!! success "Code"

	=== "html"
		```html
		<form>
			<select >
				<option name="selection" value="..." id="rien" >....</option >
				<option name="selection" value="mot 1" id="mot1" > mot 1 </option > 
				<option name="selection" value="mot 2" id="mot2"> mot 2 </option >
			</select >
		</form>
		...
		```

	=== "javascript"
		```js
		function testMenu(){
		var TexteAEcrire="vous avez sélectionné ";
		if (document.querySelector('#mot1').selected) TexteAEcrire+="le mot 1";
		if (document.querySelector('#mot2').selected) ...;
		...
		}
		```
		
!!! question "A faire"
	Compléter le code HTML et le code JS pour créer votre propre liste déroulante et afficher le résultat.

!!! note "Remarques"
	- ici le choix a été de faire apparaître une première légende vide (…) pour l'affichage par défaut (qui est la première balise `option`).  
	- il faut donner le même nom aux balises `option` mais des id différents.  


	
### Récupération de texte 
!!! example "Exemple"

	<form>
	<div id="zoneTexte">
	Entrez votre texte : <input type="text" value="" id="saisie">
	<input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" value="tester" onclick="testSaisie()">
    </div>
	</form>
	<div id="texteSaisie" ></div>

 on récupère le texte entré `value` ; on rajoute alors ce texte dans le texte (TexteAEcrire) à afficher dans le bloc d'identifiant "texteSaisie".  

!!! success "Code"

	=== "html"
		```html
			<form>
			Entrez votre texte : <input type="text" value="" id="saisie" >
			</form>
			<div id="texteSaisie" class="rajout" ></div>
		```

	=== "javascript"
		```js
		function testSaisie(){
		...
		TexteAEcrire+=document.querySelector('#saisie').value;
		...
		}
		```
!!! question "A faire"
	Compléter le code JS pour que le texte saisi par l'utilisateur s'affiche dans une phrase.

!!! note "Texte plus long"
	On peut utiliser la balise `textArea` pour un texte plus long. 


### Slide 
On peut choisir une valeur avec un curseur.  

!!! example "Exemple"

	<form>
	<div id="zoneTexte">
	<input type="range" min="1" max="100" value="50" class="slider" id="curseur">
	<input type="button" style="margin:5px; padding:5px;  background-color : lightblue; border : solid 2px blue; border-radius : 5px;" value="tester" onclick="testSlide()">
    </div>
	</form>
	<div id="textSlide" ></div>
  

!!! success "Code"

	=== "HTML"
		```HTML
		<form>
		<div id="zoneTexte">
		<input type="range" min="1" max="100" value="50" class="slider" id="curseur">
		...
	    </div>
		</form>
		...
		```

	=== "Javascript"
		```JS
		function testSlide(){
	  		var TexteAEcrire=...
	  		...
	  		...
			}
		```

!!! question "A faire"
	Compléter le code HTML et le code JS pour que la valeur choisi sur le curseur s'affiche dans un bloc sous le formulaire.

!!! question "Exercice complet"
	Créer le formulaire de votre choix en utilisant plusiers des éléments proposés et un bouton de validation qui permet d'écrire une phrase contenant les éléments récupérés.  
	Pour cet exercice, je vous déconseille fortement des aides en ligne si vous voulez etre capable de le refaire lors du devoir.  

##

---
<script>

// pour enregistrer en local
     
var contenu="";
    function enregistrer()
{
    localStorage.setItem('monTexte', JSON.stringify(contenu));	
}
    
// la fonction du bouton de la première ligne du tableau
		function ActionDuBouton()
		{
    				document.querySelector("#casecouleur").style.backgroundColor='aqua';
    	}


// la fonction qui écrit quel bouton radio a été sélectionné
		function testRadio(){
			var TexteTexteAEcrire="Le bouton radio sélectionné est le "; 
			if (document.querySelector('#radio1').checked) TexteTexteAEcrire+=1;
			if (document.querySelector('#radio2').checked) TexteTexteAEcrire+=2;
			if (document.querySelector('#radio3').checked) TexteTexteAEcrire+=3;
			if (document.querySelector('#radio4').checked) TexteTexteAEcrire+=4;
			document.querySelector('#texteRadio').textContent=TexteTexteAEcrire;
			}
		
		// la fonction qui écrit quelle(s) case(s) a (ont) été sélectionnée(s)
		function testCases(){
			var TexteAEcrire="vous avez coché ";
			if (document.querySelector('#case1').checked) TexteAEcrire+=" la case 1, ";
			if (document.querySelector('#case2').checked) TexteAEcrire+=" la case 2, ";
			if (document.querySelector('#case3').checked) TexteAEcrire+=" la case 3, ";
			document.querySelector('#texteCases').textContent=TexteAEcrire;
			}
		// la fonction qui écrit quel mot a été sélectionné
		function testMenu(){
		var TexteAEcrire="vous avez sélectionné ";
		if (document.querySelector('#mot1').selected) TexteAEcrire+="le mot 1";
		if (document.querySelector('#mot2').selected) TexteAEcrire+="le mot 2";
		document.querySelector('#texteMenu').textContent=TexteAEcrire;
		}
		
		// la fonction qui réécrit le texte saisi
		function testSaisie()
		{
		var TexteAEcrire="vous avez écrit ";
		TexteAEcrire+=document.querySelector('#saisie').value;
		document.querySelector('#texteSaisie').textContent=TexteAEcrire;
		}
		// La fonction qui donne la valeur du curseur

		function testSlide()
		{
	  		var TexteAEcrire="Vous avez choisi la valeur ";
	  		TexteAEcrire+=document.querySelector('#curseur').value;
	  		document.querySelector('#textSlide').textContent=TexteAEcrire;
		}
</script>
		

