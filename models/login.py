import sys
import os
import questionary

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
            return False

        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT role FROM users WHERE username = %s"
            cursor.execute(query, (self.username,))
            result = cursor.fetchone()

            role_value = result.get('role').lower()

            role = self.role.lower()

            print(f"Pilihan: {role}, data; {role_value}")
            if role_value == role:
                print(f"Selamat datang {self.username}")
                return role_value
            else:
                print(f"{self.username} tidak terdaftar sebagai role {role}")
        
        except Exception as e:
            print(e)

if __name__=="__main__":
    os.system('cls')
    role = questionary.select(
        'Choose your role:',
        choices = [
            "Admin",
            "Cashier",
            "Manager"
        ]
    ).ask()
    username = input("Input your username: ").lower()
    password = input("Input your password: ").lower()

    user_login = Login(username,password,role)
    user_login.ambilRole()