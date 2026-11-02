from models.menu import Menu
import questionary

class Admin(Menu):
    def __init__(self,role):
        super().__init__(role)

    def tampil_menu():
        menu_admin = questionary.select(
            
        )