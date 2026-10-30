import os
import time
import questionary
from winotify import Notification, audio
from models.login import Login

def main():
    percobaan = 0
    while True:
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
        user_login.login()
        questionary.press_any_key_to_continue().ask()

        percobaan += 1

        if percobaan >2:
            stop = 10
            notif1 = Notification(
                        app_id = "Informasi Akun",
                        title = "Jumlah percobaan masuk gagal 3",
                        msg = "Tunggu 10 detik dan coba lagi...",
                        duration = "short"
                    )
            notif1.set_audio(audio.Default, loop=False)
            notif1.show()

            for i in range(stop):
                print(f"Coba lagi dalam {i+1:02d} detik", end="\r")
                time.sleep(1)
            percobaan = 0



if __name__=="__main__":
    main()