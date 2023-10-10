# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define camille = Character('Camille Leroy, Directrice Adjointe', color="#d4ff00", role="Directrice Adjointe")
define sandrine = Character('Sandrine Chen, Responsable Logistique', color="#9b4600", role="Responsable Logistique")
define manon = Character('Manon Rousseau, Developpeur', color="#bc0081", role="Developpeur")
define frederic = Character('Frédéric Terreau, Developpeur', color="#00ff00", role="Developpeur")
define nicolas = Character('Nicolas Martin, Responsable Communication', color="#00d5ff", role="Responsable Communication")
define françois = Character('François Lefebvre, Comptable', color="#ffffff", role="Comptable")
define vincent = Character('Vincent Moreau, Manager Tech', color="#ff0000", role="Manager Tech")
define maxime = Character('Maxime Garcia, Developpeur Alternant', color="#5e5e5e", role="Developpeur Alternant")
define guillaume = Character('Guillaume Kim, Resssources Humaines', color="#ff00dd", role="Resssources Humaines")
define sebastien = Character('Sébastien Singh, Directeur', color="#1100ff", role="Directeur")
init:
    image Bureau_Direction_1 = Image("maps/Bureau_Direction_1.png", rle=False)
    image bureau = Image("maps/Bureau.jpg", rle=False)
    image director_Bureau = Image("maps/Director_Bureau.png", rle=False)
    image logi = Image("maps/Logi.png", rle=False)
    image openspace = Image("maps/Openspace.jpg", rle=False)
    image parking = Image("maps/parking.jpg", rle=False)
    image repa = Image("maps/repa.jpg", rle=False)
    image reu2 = Image("maps/reu2.jpg", rle=False)
    image reunion = Image("maps/reunion.jpg", rle=False)
    image wc = Image("maps/wc.jpg", rle=False)


# Le jeu commence ici
label start:
    scene Bureau_Direction_1

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene bureau

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene director_Bureau

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene logi

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene openspace

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene parking

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene repa

    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene reu2
    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene reunion
    camille "Vous venez de créer un nouveau jeu Ren'Py."
    scene wc

    camille "Vous venez de créer un nouveau jeu Ren'Py."

    nicolas "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    return
