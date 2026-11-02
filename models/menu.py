import os
import questionary


class Menu:
    def __init__(self,role):
        self.role = role

    def tampil_menu():
        pass

class Admin(Menu):
    def __init__(self,role):
        super().__init__(role)

    def tampil_menu():
        menu_admin = questionary.select(
            
        )