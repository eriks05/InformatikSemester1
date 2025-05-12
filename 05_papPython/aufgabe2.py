kartenStapel = ["gr7", "gl2", "+4"]
while len(kartenStapel) != 0 :
    print(kartenStapel)
    aktuelleKarte = kartenStapel.pop(0)

    if aktuelleKarte == "+4" :
        print("+4 kann gespielt werden.")
        break

if len(kartenStapel) == 0 :
    print("Stapel ist leer")


