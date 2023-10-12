label results:
    stop music
    play music "sons/guess.mp3"
    if choix == 5:
        scene parking
        "Félicitation ! Vous avez trouvé qui est le harceleur de cette entreprise."
    else:
        scene parking
        "Perdu ! Le Harceleur était François Levebvre, Comptable"
    jump flashback
