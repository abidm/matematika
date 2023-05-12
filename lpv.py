print("\t\tMenghitung Luas Permukaan dan Volume")
p = int(input('panjang : '))
l = int(input('lebar : '))
t = int(input('tinggi : '))


def luas_permukaan(p, l, t):
    lp = 2*((p*l) + (p*t) + (l*t))
    print("luas permukaannya adalah : {}".format(lp))


def volume(p, l, t):
    v = p*l*t
    print("volumenya adalah : {}".format(v))


luas_permukaan(p, l, t)
volume(p, l, t)
