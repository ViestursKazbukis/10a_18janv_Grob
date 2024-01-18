def lasit_rakstit():
    try:
        with open("1uzd.txt","r",encoding="utf8")as uzd1:
            saturs=uzd1.readlines()
            print(saturs)
        
    except FileNotFoundError:
        print("Fails netika atrasts")

if __name__=="__main__":
    lasit_rakstit()