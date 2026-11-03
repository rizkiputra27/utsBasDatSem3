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
                    Choice(title = "Kelola stok", value = "1"),
                    Choice(title = "transaksi", value = "2"),
                    Choice(title = "Keluar", value = "3"),
                ]
            ).ask()
        
       