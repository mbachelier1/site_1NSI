<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>TRANSMISSION DES DONNEES D'UN FOMRULAIRE</title>
  
  <link rel="stylesheet"  href="src/prism.css" />
	<link rel="stylesheet" href="src/main.css"/>
  
</head>
<body>
	<h1>Formulaire d'une page Web</h1>
	<h2>Introduction au php</h2>
    <p>Comme déjà évoqué dans la partie consacrée au modèle client-serveur, un serveur Web (aussi appelé serveur HTTP) permet de répondre à une requête HTTP effectuée par un client (très souvent un navigateur Web). Nous allons travailler avec le serveur Web qui est installé sur votre ordinateur ou sur votre clé USB (UwAmp). Nous allons donc avoir une configuration un peu particulière puisque le client et le serveur vont se trouver sur la même machine. Cette configuration est classique lorsque l'on désire effectuer de simples tests. Nous aurons donc 2 logiciels sur le même ordinateur : le client (navigateur Web) et le serveur (serveur Web), ces 2 logiciels vont communiquer en utilisant le protocole HTTP. Le serveur Web que nous allons utiliser se nomme "Apache", c'est un des serveur Web le plus utilisé au monde. Apache a déjà été installé et configuré sur votre ordinateur.</br>

	Nous allons commencer par un cas très simple où le serveur va renvoyer au client une simple page HTML statique
    <p class="quest"> Dans le dossier www creer un dossier "Formulaire". Puis créer dans ce répertoire un fichier "essai.html".</br>
    Copier le code ci-dessous dans le fichier créé.</p>	

	<pre class="line-numbers"><code class="language-html">&lt;!DOCTYPE html&gt;
	&lt;html&gt;
	&lt;head&gt;
	  &lt;title&gt;Utilisation d'Apache&lt;/title&gt;
	  &lt;meta charset="UTF-8" /&gt;
	&lt;/head&gt;
	&lt;body&gt;
	  &lt;p &gt;Le serveur Apache fonctionne parfaitement;&lt;/p&gt;
	&lt;/body&gt;
	&lt;/html&gt;</code></pre>
	<p class="quest">
		Exécuter UwAmp puis démarrer le serveur. Cliquer sur "Navigateur www" qui va ouvrir le dossier www dans le navigateur. Choisir le dossier Formlaire et vérifier que la page ainsi créée s'affiche.
	</p><p>Une petite explication s'impose à propos du "localhost" : comme nous l'avons déjà dit, notre serveur et notre client se trouvent sur la même machine, avec le "localhost", on indique au navigateur que le serveur Web se trouve sur le même ordinateur que lui (on parle de machine locale). Dans un cas normal, la barre d'adresse devrait être renseignée avec l'adresse du serveur Web. </p>
	<p>Pour l'instant, comme déjà dit plus haut, notre site est statique : la page reste identique, quelles que soient les actions des visiteurs. Pour avoir un site dynamique, nous allons exécuter, côté serveur, un programme qui va créer de toute pièce une page HTML, cette page HTML sera ensuite envoyée au client par l'intermédiaire du serveur Web. Il existe différents langages de programmation qui permettent de générer des pages HTML à la volée : Python, Java, Ruby... Dans notre cas, nous allons utiliser le PHP (PHP est un acronyme récursif puisqu'il signifie : PHP Hypertext Preprocessor). Le PHP est un langage très utilisé même si dans le monde professionnel Java, Python, Ruby,... sont préférés au PHP. Il est très important de bien comprendre les processus mis en oeuvre : </p>
	<ul><li>le client (le navigateur Web) envoie une requête HTTP vers un serveur Web </li>
		<li>en fonction de la requête reçue le serveur "fabrique" une page HTML grâce à l'exécution d'un programme écrit en PHP (ou en Python, Java...) </li>
		<li>le serveur Web envoie la page nouvellement créée au client </li>
		<li>une fois reçue, la page HTML est affichée dans le navigateur Web </li>
	</ul>
	<p>Le langage PHP est déjà installé sur l'ordinateur que vous utilisez actuellement, nous allons donc pouvoir écrire notre premier programme en PHP. Notez qu'il n'est pas question ici d'apprendre à programmer en PHP, mais juste d'avoir un premier contact avec ce langage (et avec cette notion de Web dynamique) </p>
	<p class='quest'>Dans le répertoire "formulaire", créez un fichier "heure.php", toujours dans le répertoire "formulaire". </br>
	Copiez le code PHP ci-dessous dans le fichier "heure.php" que vous venez de créer </p>
		<pre class="line-numbers"><code class="language-html">&lt;?php
$heure = date("H:i");
echo '&lt;h1&gt;Bienvenue sur mon site&lt;/h1&gt;
	 &lt;p&gt;Il est '.$heure.'&lt;/p&gt';
?&gt;</code></pre>
	<p class='quest'>Afficher la page.</p>
	<p> Vous devriez avoir une page HTML qui vous donne l'heure, si vous actualisez la page, vous pourrez remarquer que bien évidemment l'heure évolue. Nous avons donc bien une page dynamique : le serveur PHP crée la page Web au moment où elle est demandée. À chaque fois que vous actualisez la page, la page HTML est générée de nouveau.</br>

	Vous aurez sans doute remarqué que l'extension ".html" a été remplacée par ".php". Au moment de la requête, le programme contenu dans ce fichier a été exécuté et la page HTML a été générée. Dans les 2 cas, le fichier se nomme "index", pourquoi ? Par défaut, le serveur prend en compte un fichier nommé "index" ("index.php" ou "index.html" selon les cas). Si vous voulez nommer votre fichier autrement, il faudra modifier ce que vous avez saisi dans la barre d'adresse de votre navigateur : si par exemple vous voulez nommer votre fichier "toto.html" (ou "toto.php"), il faudra saisir dans la barre d'adresse du navigateur "localhost/toto.html" (ou "localhost/toto.php"). </p>
	<p>Quelques remarques sur le programme PHP ci-dessus : </p>
	<ul><li>"$heure = date("H:i");", "$heure" est une variable (en PHP les variables commencent par un "$"), cette variable "contient" une chaîne de caractères qui correspond à l'heure courante </li>
		<li>l'instruction "echo" permet d'afficher la chaîne de caractères qui suit l'instruction. Dans notre cas, la chaîne de caractères est 
			<pre class="line-numbers"><code class="language-html">"&lt;h1&gt;Bienvenue sur mon site&lt;/h1&gt; &lt;p&gt;Il est '.$heure.'&lt;/p&gt;"</code></pre> ce qui correspond à du HTML à l'exception de "$heure" qui permet d'afficher le contenu de la variable "$heure". La page Web générée contiendra le code HTML et le contenu de la variable "$heure". Le point "." est, en PHP, l'opérateur de concaténation (alors que par exemple en Python, l'opérateur de concaténation est le "+")  </li>
	</ul>
	<p>Si un client effectue une requête à 18h23, le serveur enverra au client le code HTML ci-dessous :</p>
	<pre class="line-numbers"><code class="language-html">&lt;h1&gt;Bienvenue sur mon site&lt;/h1&gt;
	 &lt;p&gt;Il est 18h23&lt;/p&gt;</code></pre>
<h2>Gestion des formulaires</h2>
<p class="quest">Dans le dossier "Formulaire", créez dans ce même dossier un fichier "index.html" et un fichier "trait_form.php" </p>
<p class="quest">Copiez le code HTML ci-dessous dans le fichier "index.html" que vous venez de créer : </p>
<pre class="line-numbers"><code class="language-html">&lt;!doctype html&gt;
&lt;html lang="fr"&gt;
	&lt;head&gt;
		&lt;meta charset="utf-8"&gt;
		&lt;title&gt;Le formulaire&lt;/title&gt;
	&lt;/head&gt;
	&lt;body&gt;
		&lt;form action="trait_form.php" method="post"&gt;
				&lt;label&gt;Nom&lt;/label&gt; : &lt;input type="text" name="nom" /&gt;
				&lt;label&gt;Prénom&lt;/label&gt; : &lt;input type="text" name="prenom" /&gt;
				&lt;input type="submit" value="Envoyer" /&gt;
		&lt;/form&gt;
	&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p class="quest">Copiez le code PHP ci-dessous dans le fichier "trait_form.php" que vous venez de créer :</p>
<pre class="line-numbers"><code class="language-html">&lt;?php
    $n=$_POST['nom'];
    $p=$_POST['prenom'];
    echo "&lt;p&gt;Bonjour ".$p." ".$n.", j'espère que vous allez bien.&lt;/p&gt;";
?&gt;</code></pre>
<p class="quest">Lancer la page "index.php" dans le navigateur via le serveur. Une fois la page Web affichée dans votre navigateur, remplissez le formulaire proposé et validez en cliquant sur le bouton "Envoyer" </p>
<p> Analysons le code HTML ci-dessus :</br>

Nous utilisons la balise "form" afin de mettre en place un formulaire sur notre page : </p>
<pre class="line-numbers"><code class="language-html">&lt;form action="trait_form.php" method="post"&gt;</code></pre>
<p>Nous avons 2 attributs "action" et "method". L'attribut "action="trait_form.php"" indique que le client enverra une requête HTTP vers le serveur en cas de clic sur le bouton "Envoyer". Pour répondre à cette requête du client, le serveur devra exécuter le programme PHP contenu dans le fichier "trait_form.php". Le "method="post"" nous indique que la méthode utilisée pour effectuer cette requête HTTP est une méthode "POST"</p>
<p>Au niveau des 2 balises "input" permettant de saisir le nom et le prénom : </p>
<pre class="line-numbers"><code class="language-html">&lt;label&gt;Nom&lt;/label&gt; : &lt;input type="text" name="nom" /&gt;
	&lt;label>Prénom&lt;/label&gt; : &lt;input type="text" name="prenom" /&gt;</code></pre>
<p> L'attribut "name" nous intéresse particulièrement dans ces 2 balises. Dans la première balise nous avons "name="nom"" et dans la deuxième balise, nous avons "name="prenom"". Nous aurons l'occasion de revenir sur le rôle de cet attribut "name" ci-dessous.</br>

Intéressons-nous maintenant au code contenu dans le fichier "trait_form.php" : </p>
<p>La ligne </br>
$n=$_POST['nom'];</br>
permet d'attribuer à la variable "$n" la chaîne de caractères qui a été saisie par l'utilisateur dans le formulaire : balise "input" ayant l'attribut "name="nom"". Le "nom" de "$_POST['nom']" est directement lié au "nom" de l'attribut "name="nom"". Le principe est le même pour la variable "$p" : le "prenom" de "$_POST['prenom']" est directement lié au "prenom" de l'attribut "name="prenom"". Un ""$_POST['toto']"" contiendra la chaîne de caractères saisie par l'utilisateur dans le champ correspondant à une balise "input" possédant un attribut "name="toto"". </p>
<p>La dernière ligne : </p>
<pre class="line-numbers"><code class="language-html">echo "&lt;p&gt;Bonjour ".$p." ".$n.", j'espère que vous allez bien.&lt;/p&gt;";</code></pre>
<p>ne devrait pas vous poser de problème. </p>
<p> Nous avons vu qu'un clic sur le bouton "Envoyer" déclenche une requête HTTP vers le serveur et que les informations saisies dans le formulaire sont envoyées vers le serveur (puisqu'il est possible de récupérer ces informations au niveau du code PHP : une fois de plus, le code PHP est uniquement exécuté du côté serveur). Mais comment ces informations transitent-elles entre le client et le serveur ? La réponse est simple : cela dépend de la méthode utilisée par la requête HTTP.</br>

Dans l'exemple ci-dessus, nous utilisons la méthode "POST" ("method="post""). </p>

<p class="quest">Une fois la page Web affichée dans votre navigateur, Saisissez "Sophie" pour le prénom et "Martin" pour le nom puis validez en cliquant sur le bouton "Envoyer". Une fois que vous avez cliqué sur le bouton "Envoyer", observez attentivement la barre d'adresse de votre navigateur. Vous devriez obtenir quelque chose qui ressemble à cela : </p>
<img src="src/traiform.PNG" alt="résultat du traitement du formulaire">
<p> Dans la barre d'adresse, rien de spécial à signaler, on constate que le fichier "trait_form.php" a bien été utilisé.</br>

Il est possible d'utiliser une méthode HTTP "GET" à la place de la méthode "POST".</p>
<p class="quest">Dans le fichier de formulaire, remplacer method="post" par method="get" puis dans le fichier de traitement remplacer POST par GET et refaire la même chose que précédement. Observer l'URL et noter ce qui a changé.</p>
<p> Dans le cas de l'utilisation d'une méthode "POST" les données issues d'un formulaire sont envoyées au serveur sans être directement visibles, alors que dans le cas de l'utilisation d'une méthode "GET", les données sont visibles (et accessibles) puisqu'elles sont envoyées par l'intermédiaire de l'url.</br>

Les données envoyées par l'intermédiaire d'une méthode "GET" peuvent être modifiées directement dans l'url .</p>
<p class="quest">Ouvrez votre navigateur Web et tapez dans la barre d'adresse "localhost". Une fois la page Web affichée dans votre navigateur, Saisissez "Sophie" pour le prénom et "Martin" pour le nom puis validez en cliquant sur le bouton "Envoyer". Une fois que le message "Bonjour Sophie Martin, j'espère que vous allez bien." apparait, modifier l'url : passez de "localhost/trait_form.php?nom=Martin&prenom=Sophie" à "localhost/trait_form.php?nom=Martin&prenom=Jean-Pierre", validez votre modification en appuyant sur la touche "Entrée". </p>
<p> Même si dans notre cas cette opération de modification d'url est inoffensive, vous devez bien vous douter que dans des situations plus complexes, une telle modification pourrait entrainer des conséquences plus problématiques (piratage). Il faut donc éviter d'utiliser la méthode "GET" pour transmettre les données issues d'un formulaire vers un serveur.</br>

Il est important de bien comprendre que la méthode "POST" n'offre pas non plus une sécurité absolue puisque toute personne ayant un bagage technique minimum sera capable de lire les données transmises à l'aide de la méthode "POST" en analysant la requête HTTP, même si ces données ne sont pas directement visibles dans l'url. Seule l'utilisation du protocole sécurisé HTTPS garantit un transfert sécurisé des données entre le client et le serveur (les données sont chiffrées et donc illisibles pour une personne ne possédant pas la clé de déchiffrement). </p>

<p>Pour ceux qui veulent aller plus loin dans l'utilisation du php je vous conseille l'excellent <a href="https://openclassrooms.com/fr/courses/918836-concevez-votre-site-web-avec-php-et-mysql">cours d'openclassroom</a>.</p>

	

  <script src="src/prism.js"></script>
 </body>
</html>


