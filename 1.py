def vypis_a_pridani(names):
    try:
        with open(names, 'r') as soubor:
            jmena = soubor.read().splitlines()  

        print("Existující jména:")
        for jmeno in jmena:
            print(jmeno)

        nove_jmena = ["Alexandr", "Saša", "Dulovec"]

        with open(names, 'a') as soubor:
            for nove_jmeno in nove_jmena:
                soubor.write("\n" + nove_jmeno)

        print("Nově přidaná jména:")
        for nove_jmeno in nove_jmena:
            print(nove_jmeno)

    except FileNotFoundError:
        print("Soubor nebyl nalezen.")

names = 'names.txt'
vypis_a_pridani(names)
