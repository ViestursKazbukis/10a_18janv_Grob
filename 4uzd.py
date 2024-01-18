def jauns_fails():
    try:
        # Lietotāja ievade
        faila_nosaukums = input("Ievadi faila nosaukumu: ")
        faila_paplaisinajums = input("Ievadi faila paplašinājumu: ")

        # Pilns faila nosaukums ar paplašinājumu
        fails = f"{faila_nosaukums}.{faila_paplaisinajums}"

        # Nolasīt faila saturu
        with open(fails, "r", encoding="utf8") as fails1:
            saturs = fails1.read()

        # Izdrukāt nolasīto informāciju
        print(f"\nFaila {fails} saturs:")
        print(saturs)

    except FileNotFoundError:
        print(f"Fails '{fails}' netika atrasts.")

if __name__ == "__main__":
    jauns_fails()
