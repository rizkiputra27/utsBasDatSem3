import questionary
from questionary import Choice
import os
from database.connection import get_conection

class Karyawan:
    def edit_karyawan():
        pilih_role_karyawan = questionary.rawselect(
            "Pilih Role karyawan:",
            choices = [
                Choice(title="Admin",value="1"),
                Choice(title="Kasir",value="2")
            ]
        ).ask()


    def manajemen_admin():
        menu_manajemen_admin = questionary.rawselect(
            "Pilih menu Manajemen Admin:",
            choices =[
                Choice(title="Tambah admin",value="1"),
                Choice(title="Edit admin",value="2"),
                Choice(title="Hapus admin",value="3"),
                Choice(title="Tampilkan admin",value="4"),
            ]
        ).ask()

        if menu_manajemen_admin:
            connection = get_conection()
            if connection is None:
                return 0

            try:
                cursor = connection.cursor(dictionary=True)
                query = """SELECT * FROM users"""
                cursor.execute(query)
                result = cursor.fetchall()

                return result

            except Exception as e:
                print(e)
        
    
