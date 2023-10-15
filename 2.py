def pocet_slov_v_souboru(names):
    try:
        with open(names) as soubor:
            obsah = soubor.read()
            slova = obsah.split()
            pocet_slov = len(slova)
            return pocet_slov
    except FileNotFoundError:
        return "Soubor nebyl nalezen."

names = 'names.txt'  
pocet = pocet_slov_v_souboru(names)
if isinstance(pocet, int):
    print(f"Počet slov v souboru '{names}': {pocet}")
else:
    print(pocet)
