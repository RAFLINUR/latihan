print('daftar menu')
print('pancong keju = 7000')
print('pancong coklat = 8000')
print('pancong tiramisu = 8500')
print('pancong matcha = 8500')
nama_pelanggan = str(input('Masukan nama anda : '))
menu_pancong = ['pancong keju', 'pancong coklat', 'pancong tiramisu', 'pancong matcha']
pilih_menu = str(input(menu_pancong))
harga = int(input('masukan harga : '))
beli_berapa = int(input('beli berapa : '))    
if beli_berapa > 1:
    total_harga = harga * beli_berapa
    print(total_harga)
else:
    total_harga = harga
    print(total_hargaharga)
invoice = {'Nama Pelanggan' : nama_pelanggan, 'Varian' : pilih_menu, 'Total harga': total_harga}
print(invoice)        