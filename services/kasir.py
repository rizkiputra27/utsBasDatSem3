from models.menu import Menu
import questionary
from questionary import Choice

class kasir(Menu):
    def __init__(self, role):
        super().__init__(role)

    def tampil_menu(self):
        print("=== MENU KASIR ===")
        print("1. Cek Stok")
        print("2. Transaksi")
        print("3. Keluar")
        pilih = input("Pilih menu: ")