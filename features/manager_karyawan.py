import questionary
from questionary import Choice
import os
from database.connection import get_conection

class Karyawan:
    def edit_karyawan(self):
        pilih_role_karyawan = questionary.rawselect(
            "Pilih Role karyawan:",
            choices = [
                Choice(title="Admin",value="admin"),
                Choice(title="Kasir",value="kasir")
            ]
        ).ask()

        if pilih_role_karyawan == "admin":
            self.manajemen_admin()
        else:
            self.manajemen_kasir()


    def manajemen_admin(self):
        menu_manajemen_admin = questionary.rawselect(
            "Pilih menu Manajemen Admin:",
            choices =[
                Choice(title="Tambah admin",value="1"),
                Choice(title="Edit admin",value="2"),
                Choice(title="Hapus admin",value="3"),
                Choice(title="Tampilkan admin",value="4"),
            ]
        ).ask()

        match menu_manajemen_admin:
            case "1":
                self.tampilkan_admin()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass


    def tampilkan_admin(self):
            connection = get_conection()
            if connection is None:
                return 0

            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM users WHERE role = %s"
                cursor.execute(query,("admin",))
                result = cursor.fetchall()

                # print(result)

                print(f"{'ID':^5}{'NAMA':^15}{'USERNAME':^11}{'PASSWORD':^11}{'ROLE':^7}")
                for hasil in result:
                    ID = hasil['user_id']
                    NAMA = hasil['nama']
                    USERNAME = hasil['username']
                    PASSWORD = hasil['password']
                    ROLE = hasil['role']

                    print(f"{ID:^5}{NAMA:^15}{USERNAME:^11}{PASSWORD:^7}{ROLE:^7}")

            except Exception as e:
                print(e)

    def manajemen_kasir(self):
        menu_manajemen_kasir = questionary.rawselect(
            "Pilih menu manajemen kasir:",
            choices = [
                Choice(title="Tambah kasir",value="1"),
                Choice(title="Update kasir",value="2"),
                Choice(title="Hapus kasir",value="3"),
                Choice(title="Tampilkan kasir",value="4")
            ]
        ).ask()

        if menu_manajemen_kasir:
            connection = get_conection()
            if connection is None:
                return 0

            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM users WHERE role = %s"
                query.execute(query,"cashier",)
                result = cursor.fetchall()
            except Exception as e:
                print(e)

