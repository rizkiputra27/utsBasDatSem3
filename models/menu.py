

class Menu:
    def __init__(self,role):
        self.role = role

    def tampil_menu(self):
        pass

    def pilih_menu(self):
        if self.role == "admin":
            from services.admin import Admin
            admin = Admin()
        elif self.role == "cashier":
            from services.kasir import Kasir
            kasir = Kasir()
            return kasir.tampil_menu()
        elif self.role == "manager":
            from services.manager import Manager
            manager = Manager()
            return manager.tampil_menu()
        else:
            print("Role tidak valid.")
            return None

    





