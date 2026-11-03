

class Menu:
    def __init__(self,role):
        self.role = role

    def tampil_menu(self):
        try:
            if self.role == "admin":
                from services.admin import Admin
                admin = Admin()
                admin.admin_menu()
            elif self.role == "cashier":
                from services.kasir import Kasir
                kasir = Kasir()
                kasir.kasir_menu()
            elif self.role == "manager":
                from services.manager import Manager
                manager = Manager()
                manager.manager_menu()
            else:
                print("Role tidak valid.")
                return None
        except Exception as e:
            print(e)

    





