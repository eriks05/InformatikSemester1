dayOfWeek = input("Wochentag: ")

match dayOfWeek :
    case "Montag":
        print("Montag")
    case "Dienstag":
        print("Dienstag")
    case "Samstag" | "Sonntag":
        print("Es ist Wochenende, der Tag: {dayOfWeek} die nächsten 24 Stunden")
    case _:
        print(f"Unbekannter Wochentag: {dayOfWeek}")