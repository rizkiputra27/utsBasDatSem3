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
            query = "SELECT password,role FROM users WHERE username = %s"
            cursor.execute(query, (self.username,))
            result = cursor.fetchone()

            if result is None:
                print(f"Username: {self.username} tidak ditemukan!")
            else:
                role_value = result.get('role').lower()
                password_value = result.get('password').lower()
                role = self.role.lower()

                if role_value == role and self.password == password_value:
                    print(f"Selamat DATANG {role} {self.username}")
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
    username = questionary.text("Enter your Username: ").ask().lower()
    password = questionary.password("Enter your Password: ").ask().lower()

    user_login = Login(username,password,role)
    user_login.ambilRole()