slovnik = {
    "jmeno": "Alexandr",
    "prijmeni": "Dulovec",
}

with open("slovnik.txt", "w") as soubor:
    for klic, hodnota in slovnik.items():
        soubor.write(f"{klic}: {hodnota}\n")
