label results:
    stop music
    play music "sons/guess.mp3"
    if choix == 5:
        scene parking
        "gagné"
    else:
        scene parking
        "Perdu ! Le Harceleur était François Levebvre, Comptable"
    jump flashback
