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