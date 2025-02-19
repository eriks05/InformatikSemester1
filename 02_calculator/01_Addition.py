try:
    A = int(input("Bitte geben Sie eine Zahl A ein: "))
    B = int(input("Bitte geben Sie eine Zahl B ein: "))
    C = A + B
    print("A + B = " + str(C))
except ValueError:
    print("Bitte geben Sie nur Zahlen ein!")