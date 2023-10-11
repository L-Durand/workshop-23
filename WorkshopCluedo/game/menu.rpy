screen MenuUI:
    imagemap:
        ground "maps/map.png"
        hotspot (326, 251, 349, 134) clicked Jump("bureau_direction")
        hotspot (326, 383, 349, 134) clicked Jump("bureau_comptabilite")
        hotspot (941, 252, 349, 134) clicked Jump("bureau_commercial")
        hotspot (941, 383, 349, 134) clicked Jump("bureau_logistique")
        hotspot (65, 514, 260, 191) clicked Jump("salle_reunion")
        hotspot (350, 514, 926, 300) clicked Jump("open_space")
        hotspot (1294, 250, 260, 137) clicked Jump("local")
        hotspot (1294, 390, 260, 250) clicked Jump("salle_pause")
        hotspot (1294, 640, 260, 155) clicked Jump("toilettes")
        hotspot (1555, 250, 303, 541) clicked Jump("parking")
        # Organigramme
        hotspot (57, 42, 150, 150) clicked Jump("organigramme")