from models.menu import Menu
import questionary

class kasir(Menu):
    def __init__(self, role):
        super().__init__(role)

    def tampil_menu(self):
        print("=== MENU KASIR ===")
        print("1. Cek Stok")
        print("2. Transaksi")
        print("3. Keluar")
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            print("Menampilkan stok barang")
        elif pilih == "2":
            print("Menu transaksi")
        elif pilih == "3":
            print("Keluar dari Menu Kasir")