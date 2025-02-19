loopSize = int(input("Bitte geben Sie die Anzahl der Wiederholungen ein: "))
liste = range(loopSize)
print(liste)
for i in liste:
    print("Hello World!" + str(i))

while loopSize >= 0:
    print("Hello World!" + str(loopSize))
    loopSize -= 1