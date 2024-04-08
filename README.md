# MiniStudio

 - Chacun a son dossier, même si vous êtes sur vos Branches ne touchez pas aux dossiers des autres ou ça risque de causer des merges conflicts. 
 - Pour pouvoir utiliser les trucs communs djà "finis" comme PlayerMovement ou Plateformes il faut l'avoir dans le même dossier un un dossier enfant 
	de votre fichier python. 
 - J'ai créer les premiers dossier finaux, il y a le dossier Asset dans lequel j'ai mis tous les trucs que les G.ART nous ont donnés je les ai 
	normalement bien ranger . 
 - Quand vous avez terminer une classe ou une fonction mettez le dans le dossier correspondant. 
 - Pour expliquer la hiérarchie, le fichier GameLoop.py sera la boucle de Gameplay qui appelra les autres fonction ou classes présente dans les différents
	dossiers enfants correspondant. 
 - Pour l'instant je ne sais pas ou peux aller le level éditor donc j'ai pas créer de dossier. 
 - Pour appeler des fichier python présent dans les autres dosseirs il suffit de faire (exemple PlayerMovement ) au début du code: 
	import Player.PlayerMovement
 - Quand vous faites dans modification temporaire dans votre branche pensez à bien les faire dans le dossier à votre nom. et pas en dehors.