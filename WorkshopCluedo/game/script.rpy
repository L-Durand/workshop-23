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


# Le jeu commence ici
label start:

    camille "Vous venez de créer un nouveau jeu Ren'Py."

    nicolas "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    return
