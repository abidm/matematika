a = int(input("Masukan batas bilangan : "))

print ("Ganjil")
for i in range(1, a + 1):
	if i % 2 != 0:
		print(i, end =' ')

print ('\n\n'"Genap")
for i in range (1, a + 1):
	if i % 2 == 0:
		print (i, end= ' ')