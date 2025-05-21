b = float(input("Bitte geben Sie die Breite Ihres Raumes [m] ein: "))
t = float(input("Bitte geben Sie die Tiefe Ihres Raumes [m] ein: "))
h = float(input("Bitte geben Sie die Höhe Ihres Raumes [m] ein: "))
T1 = float(input("Bitte geben Sie die Außentemperatur [°C] ein: "))
T2 = float(input("Bitte geben Sie die Innentemperatur [°C] ein: "))

V = b * t * h
dT = T2 - T1

if dT < 0:
    print("ACHTUNG DIE TEMPERATURDIFFERENZ IST KLEINER ALS NULL")

p = V * dT * 0.024
print(f"Heizleistung beträgt {p} kW")
