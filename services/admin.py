from models.menu import Menu
import questionary
from questionary import Choice

from services.kasir import Kasir

class Admin(Menu):
    def __init__(self):
        pass

    def admin_menu(self):
        menu_admin = questionary.rawselect(
            "\n===== MENU ADMIN =====",
            choices = [
                Choice(title = "Kelola Produk", value = "1"),
                Choice(title = "Kelola Stok", value = "2"),
                Choice(title = "Kelola Kasir", value = "3"),
            ]
        ).ask()

        if menu_admin == "1":
            self.tampil_produk()
        elif menu_admin == "2":
            self.tampil_stok()
        elif menu_admin == "3":
            self.kelola_kasir()
        else:
            print('Menu tidak tersedia')


    
