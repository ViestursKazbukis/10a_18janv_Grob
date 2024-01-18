def rinda3():
    try:
        with open("3uzd.txt","r",encoding='utf-8') as fails:
            rindas = fails.readlines()

            print("Rindu skaits failā:", len(rindas))

            if len(rindas) >= 3:
                print("Trešā rinda:", rindas[2])
            else:
                print("Fails nesatur vismaz trīs rindas.")

    except FileNotFoundError:
        print("Fails nav atrasts")

if __name__ == "__main__":
    rinda3()
