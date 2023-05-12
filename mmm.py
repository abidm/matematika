import statistics


jumlah = int(input("Masukan jumlah bilangan : ")) #input jumlah bilangan
print ("Masukan beberapa bilangan sesuai jumlah bilangan dengan format : [n] [n]\n") #input bilangan
data = [] #untuk menyimpan bilangan

for i in range(1, jumlah+1):
	i = int(input("[n] : "))
	data.append(int(i)) #menambahkan bilangan ke variabel data

'\n'
print ("Data yang belum di urutkan :", data)
a = sorted(data)
'\n'
print ("Data yang sudah di urutkan : ", sorted(data))
print ("Nilai median : ", statistics.median(a))
print ("Nilai Mean : ", statistics.mean(a))
print ("Nilai Modus : ", statistics.mode(a))
