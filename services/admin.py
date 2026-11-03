from models.menu import Menu
import questionary
from questionary import Choice

class Admin(Menu):
    def __init__(self):
        pass

    def tampil_menu():
        menu_admin = questionary.rawselect(
            "===== MENU ADMIN =====",
            choices = [
                Choice(title = "Kelola Produk", value = "1"),
                Choice(title = "Kelola Stok", value = "2"),
                Choice(title = "hitung pendapatan ", value = "3"),
                Choice(title = "laporan", value = "4"),
                Choice(title = "Keluar", value = "5"),
            ]
        ).ask()