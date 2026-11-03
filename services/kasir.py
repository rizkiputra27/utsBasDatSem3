from models.menu import Menu
import questionary

class kasir(Menu):
    def __init__(self, role):
        super().__init__(role)

    
        
        if pilih == "1":
            print("Menampilkan stok barang")
        elif pilih == "2":
            print("Menu transaksi")
        elif pilih == "3":
            print("Keluar dari Menu Kasir")