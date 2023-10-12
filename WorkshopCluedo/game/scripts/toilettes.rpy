label toilette:
    stop music
    queue music ["sons/toilets.mp3"]
    show screen back_black
    scene wc

    show dg at gauche_regard_1
    show adj at droite_regard_2_hide

    "*Le directeur croise la directice adjointe a l’entrée des toilettes, ils passent la porte en même temps, elle se faufile entre le directeur et la porte difficilement*"
    sebastien "Et ben alors, on a du mal a passer, c’est ça d’avoir des grosses fesses ahah"
    show dg at gauche_regard_1_hide
    show adj at droite_regard_2
    "*La directice adjointe éclate de rire devant la blague du directeur*"
    camille "Imbécile va !!! T’es vraiment bête quand tu t’y met. Si t’avais pas un bide pareil, on passerai sans soucis !!"
    show dg at gauche_regard_1
    show adj at droite_regard_2_hide
    "*Le directeur rigole a son tour*"
    show dg at gauche_regard_2
    sebastien "Aller bonne journée Camille"
    hide dg 
    show adj at droite_regard_2_hide
    "*Le directeur s’en va, l’inspecteur attend que la directrice adjointe finisse ce qu’elle est en train de faire pour lui poser une question*"
    inspecteur "Bonjour madame, permettait moi de vous poser une question, j’ai entendu la blague de Mr le directeur a votre égart, il n’y va pas un peu fort quand même ?" 
    show adj at droite_regard_2
    camille "Ahahah non pas d’inquiétude Monsieur, nous sommes amis depuis plus de 10 ans et nous avons toujours été taquins l’un envers l’autres. Il n’y a aucun soucis ne vous inquietez pas."
    show adj at droite_regard_2_hide
    inspecteur "D’accord, je comprend bien. Je voulais juste m’assurer que tout allait bien. Bonne journée Madame"
    show adj at droite_regard_2
    camille "Bonne journée à vous aussi."
    stop music fadeout 1.0
    jump carte