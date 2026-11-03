from models.menu import Menu
import questionary
from questionary import Choice

class Manager:
    def __init__(self):
        pass

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
            self.manajemen_karyawan()
        elif menu_manager == "2":
            self.manajemen_kinerja()
        else:
            print("Menu belum tersedia.")

    def manajemen_karyawan(self):
        menu_karyawan = questionary.rawselect(
            "\n===== MENU MANAJEMEN KARYAWAN =====",
            choices = [
                Choice(title = "tambah karyawan", value = "1"),
                Choice(title = "hapus karyawan", value = "2"),
                Choice(title = "ubah karyawan", value = "3"),
                Choice(title = "lihat karyawan", value = "4"),
                Choice(title = "kembali", value = "5"),
            ]
        ).ask()

        return menu_karyawan
    def manajemen_kinerja(self):
        menu_kinerja = questionary.rawselect(
            "\n===== MENU MANAJEMEN KINERJA =====",
            choices = [
                Choice(title = "lihat kinerja", value = "1"),
                Choice(title = "kembali", value = "2"),
            ]
        ).ask()

        return menu_kinerja