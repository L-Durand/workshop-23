screen MenuUI:
    imagemap:
        ground "maps/map.png"
        hotspot (326, 251, 349, 134) clicked Jump("bureau_direction") hovered ShowTransient("the_img", img="assets/check.png", x=326, y=251) unhovered Hide("the_img")
        hotspot (326, 383, 349, 134) clicked Jump("bureau_comptabilite") hovered ShowTransient("the_img", img="assets/check.png", x=326, y=383) unhovered Hide("the_img")
        hotspot (941, 252, 349, 134) clicked Jump("bureau_commercial") hovered ShowTransient("the_img", img="assets/check.png", x=941, y=252) unhovered Hide("the_img")
        hotspot (941, 383, 349, 134) clicked Jump("bureau_logistique") hovered ShowTransient("the_img", img="assets/check.png", x=941, y=383) unhovered Hide("the_img")
        hotspot (65, 514, 260, 191) clicked Jump("salle_reunion") hovered ShowTransient("the_img", img="assets/check.png", x=65, y=514) unhovered Hide("the_img")
        hotspot (350, 514, 926, 300) clicked Jump("open_space") hovered ShowTransient("the_img", img="assets/check.png", x=350, y=514) unhovered Hide("the_img")
        hotspot (1294, 250, 260, 137) clicked Jump("local") hovered ShowTransient("the_img", img="assets/check.png", x=1294, y=250) unhovered Hide("the_img")
        hotspot (1294, 390, 260, 250) clicked Jump("salle_pause") hovered ShowTransient("the_img", img="assets/check.png", x=1294, y=390) unhovered Hide("the_img")
        hotspot (1294, 640, 260, 155) clicked Jump("toilettes") hovered ShowTransient("the_img", img="assets/check.png", x=1294, y=640) unhovered Hide("the_img")
        hotspot (1555, 250, 303, 541) clicked Jump("parking") hovered ShowTransient("the_img", img="assets/check.png", x=1555, y=250) unhovered Hide("the_img")
        # Organigramme
        hotspot (57, 42, 150, 150) clicked Jump("organigramme") hovered ShowTransient("the_img", img="assets/check.png", x=57, y=42) unhovered Hide("the_img")

screen the_img(img, x, y):
    add img pos (x, y)

screen GuessUI:
    imagemap:
        ground "maps/guess_map.png"
        hotspot (833, 200, 251, 168) clicked [SetVariable("choix", 1), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=833, y=200) unhovered Hide("inculper")
        hotspot (833, 413, 251, 168) clicked  [SetVariable("choix", 2), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=833, y=413) unhovered Hide("inculper")
        hotspot (153, 620, 251, 168) clicked  [SetVariable("choix", 3), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=153, y=620) unhovered Hide("inculper")
        hotspot (492, 620, 251, 168) clicked  [SetVariable("choix", 4), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=492, y=620) unhovered Hide("inculper")
        hotspot (839, 620, 251, 168) clicked  [SetVariable("choix", 5), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=839, y=620) unhovered Hide("inculper")
        hotspot (1185, 620, 251, 168) clicked  [SetVariable("choix", 6), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=1185, y=620) unhovered Hide("inculper")
        hotspot (1514, 620, 251, 168) clicked  [SetVariable("choix", 7), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=1514, y=620) unhovered Hide("inculper")
        hotspot (153, 850, 251, 168) clicked  [SetVariable("choix", 8), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=153, y=850) unhovered Hide("inculper")
        hotspot (492, 850, 251, 168) clicked  [SetVariable("choix", 9), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=492, y=850) unhovered Hide("inculper")
        hotspot (839, 850, 251, 168) clicked  [SetVariable("choix", 10), Jump("results")] hovered ShowTransient("inculper", img="assets/check.png", x=839, y=850) unhovered Hide("inculper")

screen inculper(img, x, y):
    add img pos (x, y)