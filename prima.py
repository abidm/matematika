awal = int(input("Masukan awal bilangan : "))
akhir = int(input("Masukan akhir bilangan : "))

import math

def prima(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    for x in range(3, int(math.sqrt(i)) + 1):
        if i % x == 0:
            return False

    return True

for i in range(awal, akhir + 1):
    if prima(i):
        print ("bilangan prima : ", (i))