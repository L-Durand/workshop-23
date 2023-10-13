label park:
    stop music
    queue music ["sons/parking-sound.mp3"]
    show screen back_black
    show screen guess_black
    scene parking

    "*Le détective est dans sa voiture et entend une discution provenant de la voiture d’à côté*"

    "*Le comptable tape a la fenêtre de la voiture de la responsable logistique*"

    show compta at gauche_regard_2
    show logistique at droite_regard_1_hide
    
    françois "Salut Sandrine, tu vas bien ? Tu es ravissante aujourd’hui. Accepterais tu de venir boire un verre chez moi ce soir ? Juste un verre ne t’inquiète pas"

    show compta at gauche_regard_2_hide
    show logistique at droite_regard_1

    sandrine "non désolé je suis pas intéressée"
    
    show compta at gauche_regard_2
    show logistique at droite_regard_1_hide

    françois "Alleeeeeez, fait pas la timide, je te propose juste un petit verre"

    show compta at gauche_regard_2_hide
    show logistique at droite_regard_1

    sandrine "Non merci françois, je suis pas intéressée du tout"

    show compta at gauche_regard_2
    show logistique at droite_regard_1_hide

    françois "Alleeeeeez !!"

    show compta at gauche_regard_2_hide
    show logistique at droite_regard_1

    sandrine "Non c’est non !!"

    show compta at gauche_regard_2
    show logistique at droite_regard_1_hide

    françois "Pffff, tu sais pas ce que tu rate. Tant pis pour toi"

    show compta at gauche_regard_2_hide
    show logistique at droite_regard_1_hide
    
    "*Le comptable part en râlant et en soufflant, il semble énervé*"

    stop music fadeout 1.0
    $ parking_visited=True
    jump carte