print ("\t\t\tKALKULATOR SEDERHANA")
print ("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Hasil Bagi\n6. Pembagian dengan hasil bilangan bulat")
pilih = int(input("Pilih 1-6 : "))
while pilih > 6: #jika nilai input lebih dari 6 maka akan melakukan perulangan sampai benar
	print ("Pilihan Salah !")
	pilih = int(input("Pilih 1-6 : "))
if pilih == 1:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	h = n1+n2
	txt = "{} + {} : "
	print (txt.format(n1,n2), h)
elif pilih == 2:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	h = n1-n2
	txt = "{} - {} : "
	print (txt.format(n1,n2),h)
elif pilih == 3:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	h = n1 * n2
	txt = "{} * {} : "
	print (txt.format(n1,n2),h)
elif pilih == 4:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	h = n1 / n2
	txt = "{} / {} : "
	print (txt.format(n1,n2),h)
elif pilih == 5:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	h = n1 % n2
	txt = "{} % {} : "
	print (txt.format(n1,n2),h)
elif pilih == 6:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	h = n1 // n2
	txt = "{} // {} : "
	print (txt.format(n1,n2),h)