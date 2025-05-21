def eingabe_der_Werte():
    b = float(input("Bitte geben Sie die Breite Ihres Raumes [m] ein: "))
    t = float(input("Bitte geben Sie die Tiefe Ihres Raumes [m] ein: "))
    h = float(input("Bitte geben Sie die Höhe Ihres Raumes [m] ein: "))
    T1 = float(input("Bitte geben Sie die Außentemperatur [°C] ein: "))
    T2 = float(input("Bitte geben Sie die Innentemperatur [°C] ein: "))

    V = b * t * h
    dT = T2 - T1
    return V, dT

def berechne_Heizleistung(V_l, dT_l):
    return V_l * dT_l * 0.024

V, dT = eingabe_der_Werte()

if dT < 0:
    print(f"ACHTUNG DIE TEMPERATURDIFFERENZ IST KLEINER ALS NULL")

p = berechne_Heizleistung(V, dT)
print(f"Die benötigte Heizleistung beträgt {p} kW")
