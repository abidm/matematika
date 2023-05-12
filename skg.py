n = int (input("Masukan jumlah barang : "))

lusin = n / 12
if n % 12 == 0:
	print ("satuan lusin : ", int(lusin))
else:
	print ("satuan lusin : ", float(lusin))
kodi = n / 20
if n % 20 == 0:
	print ("satuan kodi : ",int(kodi))
else:
	print ("satuan kodi : ", float(kodi))
gross = n / 144
if n % 144 == 0:
	print ("satuan gross : ", int(gross))
else:
	print ("satuan gross : ", float(gross))