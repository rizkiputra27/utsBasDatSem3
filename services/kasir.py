from models.menu import Menu
import questionary
from questionary import Choice

class kasir(Menu):
    def __init__(self, role):
        super().__init__(role)

    def tampil_menu():
            menu_admin = questionary.rawselect(
                "===== MENU ADMIN =====",
                choices = [
                    Choice(title = "menampilkan stok", value = "1"),
                    Choice(title = "transaksi", value = "2"),
                    Choice(title = "keluar", value = "3"),
                ]
            ).ask()
        