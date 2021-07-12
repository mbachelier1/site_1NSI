#Le modèle d'architecture de Von Neumann et les systèmes d'exploitaion
##Un peu d'histoire...
###Les précurseurs
<div>
		<img class="inl" align="right" src="../src/images/turing.png" alt='Alan Turing' title="Alan Turing">  
</div>
Les travaux du mathématicien anglais Alan Turing (1912-1954) à la fin des années 30 ont été fondateurs de l’informatique ; Alan Turing est connu pour son rôle pendant la Seconde Guerre Mondiale dans le déchiffrement des messages de la machine Enigma de l’armée allemande. Il travaille en particulier sur les concepts de programmation et d’intelligence artificielle.
<div>		<img  align="left" class="inl" src="../src/images/von neumann.png" alt='John Von Neumann' title="John Von Neumann"></div>
Ces travaux ont inspiré un mathématicien et physicien hongrois naturalisé américain : John Von Neumann (1903-1957). Il énonce en 1945 les principes d’architecture d’un ordinateur.
Les ordinateurs actuels fonctionnent encore sous ce principe, que l’on appelle donc l’architecture de Von Neumann.
<div>	<img align="right" class="inl" src="../src/images/shannon.png" alt='Claude Shannon' title='Claude Shannon'></div>
Claude Shannon (1916-2001) ingénieur américain en électricité et mathématicien, apporte une théorie de l’information et de la communication dans les mêmes années. Il est l’un des premiers a utiliser le mot "bit".  
		
!!! important "Vocabulaire"

	- le mot anglais "computer" vient du latin computare qui signifie compter.  
	- le mot "informatique" a été créé en 1962 avec les mots information et automatique (par Philippe Dreyfus)  
	- le mot "ordinateur" a été créé en 1955 par Jacques Perret linguiste et professeur à la Sorbonne. 

Il y a 58 ans, le 16 avril 1955, le mot ordinateur était inventé par le professeur de philologie (l'étude d'une langue et de sa littérature à partir de documents écrits) Jacques Perret. 
Son origine est une demande d’IBM, qui voulait un nom français plus parlant que « calculateur » pour sa nouvelle machine électronique destinée au traitement de l'information (IBM 650) en évitant d'utiliser la tra-duction littérale du mot anglais computer (« calculateur » ou « calculatrice »), qui était à cette époque plutôt réservé aux machines scientifiques. 


!!! cite "Voici la lettre envoyée par Jacques Perret à IBM, qui a officialisé le nom ordinateur."
	Cher Monsieur,  
	Que diriez-vous d’ordinateur? C’est un mot correctement formé, qui se trouve même dans le Littré comme adjectif désignant Dieu qui met de l’ordre dans le    monde. Un mot de ce genre a l’avantage de donner aisément un verbe ordiner, un nom d’action ordination. L’inconvénient est que ordina-tion désigne une cérémonie religieuse ; mais les deux champs de signification (religion et comp-tabilité) sont si éloignés et la cérémonie d’ordination connue, je crois, de si peu de personnes que l’inconvénient est peut-être mineur. D’ailleurs votre machine serait ordinateur (et non ordination) et ce mot est tout à fait sorti de l’usage théologique. Systémateur serait un néologisme, mais qui ne me paraît pas offensant ; il permet systématisé ; — mais système ne me semble guère utilisable — Combinateur a l’inconvénient du sens péjoratif de combine ; combiner est usuel donc peu ca-pable de devenir technique ; combination ne me paraît guère viable à cause de la proximité de combinaison. Mais les Allemands ont bien leurs combinats (sorte de trusts, je crois), si bien que le mot aurait peut-être des possibilités autres que celles qu’évoque combine.
	Congesteur, digesteur évoquent trop congestion et digestion. Synthétiseur ne me paraît pas un mot assez neuf pour désigner un objet spécifique, déterminé comme votre machine.  
	En relisant les brochures que vous m’avez données, je vois que plusieurs de vos appareils sont désignés par des noms d’agent féminins (trieuse, tabulatrice). Ordinatrice serait parfaitement pos-sible et aurait même l’avantage de séparer plus encore votre machine du vocabulaire de la théo-logie. Il y a possibilité aussi d’ajouter à un nom d’agent un complément : ordinatrice d’éléments complexes ou un élément de composition, par exemple : sélecto-systémateur. Sélecto-ordinateur a l’inconvénient de deux o en hiatus, comme électro-ordinatrice.  
	Il me semble que je pencherais pour ordinatrice électronique. Je souhaite que ces suggestions stimulent, orientent vos propres facultés d’invention.  N’hésitez pas à me donner un coup de télé-phone si vous avez une idée qui vous paraisse requérir l’avis d’un philologue.  
	Vôtre   
	Jacques Perret  



###Le premier ordinateur
<div><img align="right" class="inl" src="../src/images/eniac.png" alt='Eniac' title='ENIAC'></div>

L’ENIAC — Electronic Numerical Integrator and Computer — fut le premier calculateur entièrement électronique ayant les mêmes capacités qu’une machine de Turing, aux limites physiques près. Il fut opérationnel à la fin de l’année 1945. 
Il avait des dimensions imposantes : plus de 20 m de long, 2,50 m de haut, 30 tonnes. Comportant 18 000 tubes électroniques, il consommait 150 kilowatts. 
Les données étaient lues sur cartes perforées. Pour programmer une application (initialement, le calcul de tables de tir pour l’artillerie), il fallait faire un plan des connexions nécessaires, puis procéder au câblage physique, un travail long, fastidieux, et sujet aux erreurs. La détection et la correction des fautes étaient également laborieuses. Avec la fiabilité réduite des tubes électroniques, ce mode de programmation constituait le grand point faible du projet. 
Bien conscients de cette faiblesse, ses concepteurs ont commencé dès 1944 à réfléchir à l’étape suivante, avant même la mise en service de l’ENIAC.

!!! faq "questions"
	1. Quel est l'âpport principal de Turing?  
	2. Quel est l'apport principal de Von Neumann?  



##Architecture de Von Neumann
<div>
<img align="right" class="inl" src="../src/images/archi VN.png" alt='Modele de Von Neumann' title="Modele de Von Neumann"></div>
L’architecture de von Neumann est un modèle structurel d’ordinateur dans lequel une unité de stockage (mémoire) unique sert à conserver à la fois les instructions et les données demandées ou produites par le calcul. Les ordinateurs actuels sont tous basés sur des versions améliorées de cette architecture.  
  
</br>
</br>
!!! summary "L’architecture de von Neumann décompose l’ordinateur en 4 parties distinctes : "
	
	- l’unité arithmétique et logique (UAL ou ALU en anglais) ou unité de traitement : son rôle est d’effectuer les opérations de base ;  	
	- l’unité de contrôle ou de commande (control unit), chargée du « séquençage » des opérations ;  
	- la mémoire qui contient à la fois les données et le programme qui indiquera à l’unité de contrôle quels sont les calculs à faire sur ces données ;  
	- les dispositifs d’entrée-sortie, qui permettent de communiquer avec le monde extérieur.  


!!! note "Remarques" 
	
	- Les différents éléments échangent des informations à l’aide de bus  (un bus peut être un ensemble de câbles qui transmettent simultanément les informations mais aussi l'ensemble des informations transmises).  
	<div><img align="right" class="inl" src="../src/images/bus.png" alt='les différents types de bus' title='Les différents types de bus'></div>
	- On peut trouver la vitesse d’horloge dans windows en cherchant "informations système" et on trouve un résultat en GHz (GigaHertz). </br>
	Un hertz est la mesure de la fréquence de répétition d'un événement qui se répète une fois par seconde. Donc   1 GHz = 10<sup>9</sup> Hz</br>
	Par exemple une horloge en 2GHz fait 2.109 opérations par seconde c’est à dire une opération toutes les 0,5 nanoseconde. (1 nanoseconde = 10<sup>-9</sup> secondes).  
	- La première innovation de la machine de Von Neumann est la séparation nette entre l’unité de commande, qui organise le flot de séquencement des instructions, et l’unité arithmétique, chargée de l’exécution proprement dite de ces instructions.  
	- La seconde innovation, la plus fondamentale, est l’idée du programme enregistré : les instructions, au lieu d’être codées sur un support externe (ruban, cartes, tableau de connexions), sont enregistrées dans la mémoire selon un codage conventionnel. Un emplacement de mémoire peut contenir indifféremment des instructions et des données, et une conséquence majeure est qu’un programme peut être traité comme une donnée par d’autres programmes. Cette idée, présente en germe dans la machine de Turing, trouvait ici sa concrétisation.  

!!! faq "Questions"
	5.En faisant éventuellement une recherche complémentaire, comment étaient apportés le programme informatique avant sa présence dans l'unité de mémoire?  
	6.Quelle est la différence entre mémoire volatile et permanente?   
	7.Résumer en quelques lignes ce que fait le processeur?  
	8.Quelle est la différence entre un processeur monoprocessus et multiprocessus?

##Composants d'une machine
###Vue d'ensemble
Dans cette partie, nous considérerons une machine informatique au sens large : ordinateur de bureau, ordinateur portable, smartphone, tablette …  
Physiquement une machine informatique est constituée de plusieurs éléments :

-	Une carte mère avec un microprocesseur, une carte graphique, des barrettes mémoires, une carte réseau, des ports (=prises)…  
-	Des périphériques qui peuvent être internes ou externes : disques durs, écran, clavier ...  

###Les mémoires

Il y a des mémoires de plusieurs types :

-	La "mémoire morte" , en anglais ROM (Read Only Memory). Mémoire de toute petite capacité accessible uniquement en lecture et modifiée une fois pour toute à la fabrication de l’ordinateur. C’est une mémoire non volatile contenant juste le nécessaire pour faire démarrer l’ordinateur.  
-	La "mémoire vive", en anglais RAM (Random Access Memory). Mémoire de capacité moyenne (quelques Go) est une mémoire volatile, c’est à dire que son contenu s’efface lorsque l’on éteint l’ordinateur. Elle stocke les données et les programmes durant l’exécution par le processeur.  
-	La "mémoire de masse" : tout système permettant d’effectuer des sauvegardes, mémoire donc non volatile, stocke les données et les programmes.  

!!! faq "questions"
	9.Citer des exemples de mémoires de masse.  
	10.Donner des exemples de périphériques avec lesquels le processeur peut etre amené à communiquer.   

###Pour aller plus loin ...
<div id="center">
<iframe  width="560" height="315" src="https://www.youtube.com/embed/c9pL_3tTW2c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


----
## Les systèmes d'exploitation

###A quoi sert un OS ?
Visionner la vidéo ci-dessous :
<div id="center">
<a href="https://youtu.be/4OhUDAtmAUo"><img src="https://framabook.org/wordpress/wp-content/uploads/2015/07/Framabook7couv450x300.jpg" alt="Histoire des OS"></a></div>
			
!!! faq "Questions"
	1.Que signifie OS?
	2.Citer les OS que vous connaissez.
	3.Quels sont les services rendus par un OS?


###Histoire de UNIX
<div id="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Za6vGTLp-wg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
Le système UNIX est un système dit "propriétaire" (certaines personnes disent "privateur"), c'est-à-dire un système non libre. Mais plus généralement, qu'est-ce qu'un logiciel libre ?
D'après Wikipédia : "Un logiciel libre est un logiciel dont l'utilisation, l'étude, la modification et la duplication par autrui en vue de sa diffusion sont permises, techniquement et légalement, ceci afin de garantir certaines libertés induites, dont le contrôle du programme par l'utilisateur et la possibilité de partage entre individus". Le système UNIX ne respecte pas ces droits (par exemple le code source d'UNIX n'est pas disponible, l'étude d'UNIX est donc impossible), UNIX est donc un système "propriétaire" (le contraire de "libre"). Attention qui dit logiciel libre ne veut pas forcement dire logiciel gratuit (même si c'est souvent le cas), la confusion entre "libre" et "gratuit" vient de l'anglais puisque "free" veut à la fois dire "libre", mais aussi gratuit.   

!!! faq "Questions"
		4.Citer des logiciels libres que vous connaissez.</br>
		5.Parmis les OS cités dans la première partie, lesquels sont libres? Lesquels sont gratuits?.</br></p>

###Et les autres
<div id="center">
		<iframe width="560" height="315" src="https://www.youtube.com/embed/IquNF_DXcF8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
Microsoft a été créée par Bill Gates et Paul Allen en 1975. Microsoft est surtout connue pour son système d'exploitation Windows. Windows est un système d'exploitation "propriétaire", la première version de Windows date 1983, mais à cette date Windows n'est qu'un ajout sur un autre système d'exploitation nommé MS-DOS. Aujourd'hui Windows reste le système d'exploitation le plus utilisé au monde sur les ordinateurs grand public.  
Enfin pour terminer, quelques mots sur le système d'exploitation des ordinateurs de marque Apple : tous les ordinateurs d'Apple sont livrés avec le système d'exploitation macOS. Ce système macOS est un système d'exploitation UNIX, c'est donc un système d'exploitation propriétaire.  

!!! faq "Question"
		6.Où retrouve-t-on presque systématiquement un OS linux?
	
