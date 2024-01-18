def uzd5():
    try:
        vards = input("Ievadi savu vārdu: ")

        with open("uzd5.txt", "w", encoding="utf8") as fails:
            fails.write(vards)

    except FileNotFoundError:
        print("Fails netika atrasts")
    except (ValueError, IndexError):
        print("tu esi nokļūdijiesss")

if __name__ == "__main__":
    uzd5()