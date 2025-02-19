while True:
    print("Wenn Sie zwei Zahlen addieren wollen, schreiben Sie 'Add'.")
    print("Wenn Sie zwei Zahlen voneinander subtrahieren wollen, schreiben Sie 'Sub'.")
    print("Wenn Sie zwei Zahlen multiplizieren wollen, schreiben Sie 'Mul'.")
    print("Wenn Sie zwei Zahlen dividieren wollen, schreiben Sie 'Div'.")
    print("Wenn Sie das Programm beenden wollen, schreiben Sie 'Exit")
    operation = input("Welche Operation wollen Sie durchführen? ")

    if operation == "Add":
        try:
            A = int(input("Bitte geben Sie eine Zahl A ein: "))
            B = int(input("Bitte geben Sie eine Zahl B ein: "))
            print("A + B = " + str(A + B))
        except ValueError:
            print("Bitte geben Sie nur Zahlen ein!")
    elif operation == "Sub":
        try:
            A = int(input("Bitte geben Sie eine Zahl A ein: "))
            B = int(input("Bitte geben Sie eine Zahl B ein: "))
            print("A - B = " + str(A - B))
        except ValueError:
            print("Bitte geben Sie nur Zahlen ein!")
    elif operation == "Mul":
        try:
            A = int(input("Bitte geben Sie eine Zahl A ein: "))
            B = int(input("Bitte geben Sie eine Zahl B ein: "))
            print("A * B = " + str(A * B))
        except ValueError:
            print("Bitte geben Sie nur Zahlen ein!")
    elif operation == "Div":    
        try:
            A = int(input("Bitte geben Sie eine Zahl A ein: "))
            B = int(input("Bitte geben Sie eine Zahl B ein: "))
            while B == 0:
                B = int(input("Bitte geben Sie eine Zahl B ungleich 0 ein: "))
            print("A/B = " + str(A/B))
            print("A/B ganzzahlig: " + str(A//B))
            print("Rest: " + str(A % B))
        except ValueError:
            print("Bitte geben Sie nur Zahlen ein!")
    elif operation == "Exit":
        print("Programm wird beendet.")
        break
    else:
        print("Bitte geben Sie eine gültige Operation ein!")
