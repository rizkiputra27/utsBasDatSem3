from models.menu import Menu
import questionary
from questionary import Choice

class Manager:
    def __init__(self, role):
        super().__init__(role)

    def tampil_menu():
        menu_manager = questionary.rawselect(
            "===== MENU MANAGER =====",
            choices = [
                Choice(title = "manajemen karyawan", value = "1"),
                Choice(title = "manajemen kinerja", value = "2"),
                Choice(title = "lihat laporan", value = "3"),
                Choice(title = "keluar", value = "4"),
            ]
        ).ask()

        return menu_manager

    def manajemen_karyawan():
        menu_karyawan = questionary.rawselect(
            "===== MENU MANAJEMEN KARYAWAN =====",
            choices = [
                Choice(title = "tambah karyawan", value = "1"),
                Choice(title = "hapus karyawan", value = "2"),
                Choice(title = "ubah karyawan", value = "3"),
                Choice(title = "lihat karyawan", value = "4"),
                Choice(title = "kembali", value = "5"),
            ]
        ).ask()

        return menu_karyawan
    def manajemen_kinerja():
        menu_kinerja = questionary.rawselect(
            "===== MENU MANAJEMEN KINERJA =====",
            choices = [
                Choice(title = "lihat kinerja", value = "1"),
                Choice(title = "kembali", value = "2"),
            ]
        ).ask()

        return menu_kinerja