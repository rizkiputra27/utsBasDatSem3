from features.admin_produk import Produk
from models.menu import Menu
import questionary
from questionary import Choice

from services.kasir import Kasir

class Admin(Menu):
    def __init__(self):
        pass

    def admin_menu(self):
        menu_admin = questionary.rawselect(
            "\n===== MENU ADMIN =====",
            choices = [
                Choice(title = "Kelola Produk", value = "1"),
                Choice(title = "Kelola Stok", value = "2"),
                Choice(title = "Kelola Kasir", value = "3"),
            ]
        ).ask()

        if menu_admin == "1":
            self.tampil_produk()
        elif menu_admin == "2":
            self.tampil_stok()
        elif menu_admin == "3":
            self.kelola_kasir()
        else:
            print('Menu tidak tersedia')


    def tampil_produk(self):
        menu_produk = questionary.rawselect(
        "\n===== MENU PRODUK =====",
        choices = [
            Choice(title = "Tambah Produk", value = "1"),
            Choice(title = "Update Produk", value = "2"),
            Choice(title = "Hapus Produk", value = "3"),
            Choice(title = "Tampilkan Produk", value = "4"),
            Choice(title = "Keluar", value = "5")
        ]
        ).ask()

        if menu_produk:
            from features.admin_produk import Produk
            produk = Produk()
            if menu_produk == "1":
                produk.tambah_produk()
            elif menu_produk == "2":
                produk.update_produk()
            elif menu_produk == "3":
                produk.hapus_produk()
            elif menu_produk == "4":
                produk.tampilkan_produk()
            else:
                print("perintah tidak diketahui.")

    def tampil_stok(self):
        menu_stok = questionary.rawselect(
            "\n===== MENU STOK =====",
            choices = [
                Choice(title="Tambah Stok", value = "1"),
                Choice(title="Update Stok", value = "2"),
                Choice(title="Hapus Stok", value = "3"),
                Choice(title="Keluar", value = "4"),
            ]
        ).ask()

        if menu_stok:
            from features.admin_produk import Produk
            produk = Produk()
            if menu_stok == "1":
                produk.tambah_stok()
            elif menu_stok == "2":
                produk.update_stok()
            elif menu_stok == "3":
                produk.hapus_stok()
            else:
                print("perintah tidak diketahui.")

    def kelola_kasir(self):
        menu_kasir = questionary.rawselect(
            "\n===== MENU KASIR =====",
            choices = [
                Choice(title = "Tambah Kasir", value = "1"),
                Choice(title = "Edit Kasir", value = "2"),
                Choice(title = "Hapus Kasir", value = "3"),
                Choice(title = "Lihat Kasir", value = "4"),
                Choice(title = "Keluar", value = "5"),
            ]
        ).ask()

        if menu_kasir:
            from features.admin_kasir import Kasir
            kasir = Kasir()
            if menu_kasir == "1":
                kasir.tambah_kasir()
            elif menu_kasir == "2":
                kasir.edit_kasir()
            elif menu_kasir == "3":
                kasir.hapus_kasir()
            elif menu_kasir == "4":
                kasir.lihat_kasir()
            else:
                print("perintah tidak diketahui.")