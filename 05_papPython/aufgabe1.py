import random

anzWurf = 0
while anzWurf <3:
    anzWurf = anzWurf + 1
    wurf = random.randint(1,6)
    print(wurf)
    if wurf == 6:
        break
if wurf == 6:
    while wurf == 6 and anzWurf <3 :
        anzWurf = anzWurf + 1
        wurf = random.randint(1,6)
        print(wurf)
