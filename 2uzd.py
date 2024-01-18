import csv

def kolona2():
    try:
        with open("uzd2.csv", 'r', encoding='utf-8') as fails:
            lasit = fails.readlines()
            
            for rinda in enumerate(lasit):
                    if len(rinda) >= 3:
                        print(rinda[2])
    
    except FileNotFoundError:
        print("Fails netika atrasts")

if __name__ == "__main__":
    kolona2()
