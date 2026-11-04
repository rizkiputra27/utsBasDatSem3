from models.menu import Menu
import questionary
from questionary import Choice

class Kasir(Menu):
    def __init__(self):
        pass

    def kasir_menu(self):
        menu_kasir = questionary.rawselect(
            "\n===== MENU ADMIN =====",    
            choices = [
                Choice(title = "Kelola stok", value = "1"),
                Choice(title = "transaksi", value = "2"),
                Choice(title = "Keluar", value = "3"),
            ]
        ).ask()
        
        if menu_kasir:
            from features.kasir_kelola_stok import Stok
            stok_kasir = Stok()
            if menu_kasir == "1":
                stok_kasir.kelola_stok()
            elif menu_kasir == "2":
                stok_kasir.transaksi()
            else:
                print("Masukkan menu yang benar.")