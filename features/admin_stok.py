import questionary
from questionary import Choice
import os


class Stok:
    def tampil_stok(self):
            menu_stok = questionary.rawselect(
                "\n===== MENU STOK =====",
                choices = [
                    Choice(title="Tambah Stok", value = "1"),
                    Choice(title="Update Stok", value = "2"),
                    Choice(title="Hapus Stok", value = "3"),
                    choice(litle="Lihat stok", value = "4")
                    Choice(title="Keluar", value = "5"),
                ]
            ).ask()
    
            if menu_stok:
                from features.admin_stok import Stok
                stok = Stok()
                if menu_stok == "1":
                    stok.tambah_stok()
                elif menu_stok == "2":
                    stok.update_stok()
                elif menu_stok == "3":
                    stok.hapus_stok()
                elif menu_stok == "4":
                    stok.lihat_stok()
                else:
                    print("perintah tidak diketahui.")
    
    def tambah_stok():
        pass
    def update_stok():
        pass
    def hapus_stok():
        pass
    def lihat_stok():
        pass