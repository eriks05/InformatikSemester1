import random

anzVersuche = 0
print("Wollen Sie sich freikaufen?")
freikaufen = (input("Bitte geben Sie ja oder nein ein: "))
if freikaufen == "ja":
    print("Sie haben sich freigekauft")
else:
    while anzVersuche < 3:
        wurf1 = random.randint(1,6)
        wurf2 = random.randint(1,6)
        print(wurf1)
        print(wurf2)
        if wurf1 == wurf2:
            print("Sie kommen frei!")
            break
        anzVersuche = anzVersuche+1
        print("Sie dürfen nochmal würfeln")
    if anzVersuche >= 3:
        print("Sie müssen zahlen!")
