# Projet
Toutes les informations qui m'ont été utile à la création de mon projet de fin d'étude seront stockés ici.

Tout ce qu'il y a été fait du 02-03-2021 à 06-03-2021

Réception des différents colis:

 -Raspberry pi 4 4GO de ram avec pleins d'accessoire utile.
 
 -le controlleur Esp8266
 
 -2x LED MAX7219
 
 

--------------------------------------------------------------------------------------------------------------------------
Découverte du raspberry pi et de son environnement, activation du VNC et SSH pour une prise en main
facile à partir de mon pc principale.

Testing des leds en affichant des mots dessus, tout semble fonctionner parfaitement.


Création d'un site web avec joomla (peux être utile par la suite ?) Le nom du domain est dek-it.be


---------------------------------------------------------------------------------------------------------------------------
UPDATE DU 08-03-21

J'ai réussi à faire une requête à l'api ! Cela m'a pris deux jours pour comprendre (le site est absolument pas intuitif,
j'avais plusieurs clé et pour s'abonner à la partie de l'api qui m'intérresse était buggé)
MAIS je l'ai fait ! Et c'est le plus important !

Maintenant il faut """""""""""""""""""""""""juste""""""""""""""""""""""""""" que je traite les données que j'ai obtenues,
car je sais déjà afficher du texte sur ma led.






-------------------------------------------------------------------------------------------------------------------------
24/03/2021

Bon avancement dans le projet, j'ai trouver un bon moyen de "parser" le code
en json que je reçois lorsque je fais une requête à l'API en C.

---------------------------------------------------------------------------------------------------------
03-04-21

Je continue sur ma lancée, j'ai eu quelques soucis avec le code, mais j'ai réussi à les régler.
Maitenant les réponses des requête que je fais s'enregistre automatiquement dans des fichiers spécifiques.

(PS: j'ai upload mon main.py sur github !)

----------------------------------------------------------------------------------------------------------
07-05-21

Oulà, il y a beaucoup de choses à dire ! Je vais essayer de rester concis.
Je suis passer d'arduino vers micropython car:

-Plus simple à comprendre/ rapide dans l'éxecution

-Je peux controller ET ma matrice led ET les leds en même temps (c'était bugger sous arduino)


J'ai rencontrer plusieurs soucis, le gros plus probléme était de faire afficher le texte que je reçevais de mon code en python, c'était très ennyant
car sous arduino, je voyais vraiment pas comment l'implementer (et pleins de gens disaient que c'était trop dur voir impossible avec arduino)
je me suis donc trourner vers micropython, j'ai eu là aussi beaucoup de soucis mais je les réglais beaucoup plus rapidement que sous arduino
en voici quelques uns;



Code qu'il fallait retaper sous arduino (car pas adapté à mon hardware ou juste des
faut de typo qui fait tout capoter)

L'app geany qui fonctionne pas avec python3, je passe donc sous pycharm

pycharm detecte pas l'esp8266 (

Mauvais package/libraires = outdated

Impossible de continuer avec le firmware de 

micropython (pas detecter sur pycharm)

je remet le firmware de base car j'ai trouver une libraire qui pouvais
marcher avec l'os de base

MICROPYTHOn QUI DEMANDE PLEINS DE PACKAGE DIFFERENT SINON IL FONCTIONNE PAS

Reinstallation de micropython car la libraire que j'ai tester fonctionnais pas

carte plus detecter sur mon pc principale(Soucis au niveau des Drivers)


J'ai finalement réussi à tout faire fonctionner( donc; chercher les infos grâce à l'api, traiter les données, le flasher sur la carte de dev. 
avec le code pour cette carte + la librairie et faire afficher le tout sur ma matrice led). J'ai aussi créer un petit script en shell 
pour automatiser le tout

j'ai utilisé la librairie de 
https://github.com/jgbrown32/ESP8266_MAX7219
qui lui même c'est basé sur ces libraires;

Vincent Rialland : https://github.com/vrialland/micropython-max7219
Mike Causer : https://github.com/mcauser/micropython-max7219
joewez : https://github.com/joewez/WifiMarquee
Merci à vous !
