#Coder le texte
##encodage du texte
Chaque caractère est encoder en binaire selon la norme ASCII
![ascii](https://pixees.fr/informatiquelycee/n_site/img/ASCII.svg)

L'ascii permet de coder tous les caratères de base de la langue anglaise mais pose des problème pour les langues comme le français puisqu'elle ne tient pas compte des accents et pour les langues avec un alphabet différent.
Il exciste pour cela l'UNICODE qui permet sur 1 (UTF-8), 2 (UTF-16) ou 4 (UTF-32) octets de coder tous les caratères existants.  
Cela dit l'unicode UTF-8 le plus utilisé a le même encodage que l'ascii.

##En python

###Fonction `ord()`  

La fonction ord() renvoie le valeur représentant l'unicode d'un caractère spécifié. Si la longueur du chaîne est supérieure à un, une erreur « TypeError » sera déclenchée.

###Fonction `chr()`  
Renvoie la chaîne représentant un caractère dont le code de caractère Unicode est le nombre entier i. Par exemple, `chr(97)` renvoie la chaîne de caractères 'a', tandis que chr(8364) renvoie '€'. Il s'agit de l'inverse de `ord()`.


###Petit mémo utilse pour le TP
!!! note "mémo"
	
	`‘0xFE5’` : représentation en hexadécimal de la valeur FE5  
	`‘0b0101’` : représentation binaire  
	`hex(54)` : converti un entier décimal en hexadécimal  
	`bin(54)` : converti l’entier en binaire  
	`str ()` : change un nombre en chaine de caractère  
	`int()` : change une chaine de caractère en un entier  