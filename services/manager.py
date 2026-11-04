# from models.menu import Menu
import questionary
from questionary import Choice
class Manager:
    def manager_menu(self):
        menu_manager = questionary.rawselect(
            "\n===== MENU MANAGER =====",
            choices = [
                Choice(title = "manajemen karyawan", value = "1"),
                Choice(title = "manajemen kinerja", value = "2"),
                Choice(title = "lihat laporan", value = "3"),
                Choice(title = "keluar", value = "4"),
            ]
        ).ask()

        if menu_manager == "1":
            from features.manager_karyawan import Karyawan
            manager_karyawan = Karyawan()
            manager_karyawan.edit_karyawan()
        elif menu_manager == "2":
            pass
        else:
            print("Menu belum tersedia.")