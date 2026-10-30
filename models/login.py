import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_conection

class Login:
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role

    def ambilRole(self):
        connection = get_conection()
        if connection is None:
            return 0

        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT password,role FROM users WHERE username = %s"
            cursor.execute(query, (self.username,))
            result = cursor.fetchone()

            return result
        
        except Exception as e:
            print(e)

    def login(self):
        result_role = self.ambilRole()
        waktu_login = datetime.now()


        if result_role is None:
            print(f"Username: {self.username} tidak ditemukan!")
        else:
            role_value = result_role.get("role").lower()
            password_value = result_role.get('password').lower()
            role = self.role.lower()

            if role_value == role and self.password == password_value:
                print(f"Selamat DATANG {role} {self.username}")
                print(f"Waktu login {waktu_login.strftime("%d %B %Y - %H:%M")}")
                return role_value
            else:
                print(f"{self.username} tidak terdaftar sebagai role {role}")

