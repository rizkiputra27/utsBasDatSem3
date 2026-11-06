import questionary
from questionary import Choice
import os
from database.connection import get_conection


class Produk:
    def sambung(self):
        self.connection = get_conection()


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

    def tambah_produk(self):
        cursor = connection.cursor(dictionary=True)
        sql = """
        INSERT INTO products
        (product_id, category_id, nama, cost_price, selling_price, stock, min_stock)
        VALUES(%s,%s,%s,%s,%s)
        """
    def update_produk(self):
        cursor = connection.cursor(dictionary=True)
        sql = """
        SET
            UPDATE products
            category_id = %s,
            nama = %s,
            cost_price = %s,
            selling_price = %s,
            stock = %s,
            min_stock = %s
        
        WHERE product_id = %s 
        """

    def hapus_produk(self):
        cursor = connection.cursor(dictionary=True)
        sql = "DELETE FROM products WHERE id = %s"
    def tampilkan_produk(self):
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM products"
        
        


