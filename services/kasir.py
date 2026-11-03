from models.menu import Menu
import questionary
from questionary import Choice

class Kasir(Menu):
    def __init__(self, role):
        super().__init__(role)

    def tampil_menu():
        menu_kasir = questionary.rawselect(
            "===== MENU ADMIN =====",    
            choices = [
                Choice(title = "Kelola stok", value = "1"),
                Choice(title = "transaksi", value = "2"),
                Choice(title = "Keluar", value = "3"),
            ]
        ).ask()
        
        return menu_kasir