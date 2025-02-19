dayOfWeek = input("Bitte geben Sie den Wochentag ein: ")
time = int(input("Bitte geben Sie die aktuelle Uhrzeit ein (als ganze Zahl): "))

if dayOfWeek == "Montag" :
    print("Heute ist Montag!")
    if time < 9:
        print("Guten Morgen!")
    elif time < 15:
        print("Frohes arbeiten!")
    else:
        print("Guten Abend!")
elif dayOfWeek == "Dienstag":
    print("Heute ist Dienstag!")
else:
    print("Heute ist nicht Montag oder Dienstag!")