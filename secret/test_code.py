from winotify import Notification, audio
import time
import questionary

notif1 = Notification(
                app_id = "Informasi Akun",
                title = "Akun anda telah terblokir",
                msg = "Hubungi akun untuk membuka kembali",
                duration = "short"
            )
notif1.set_audio(audio.Default, loop=False)
notif1.show()
stop = 10
for i in range(stop):
    print(f"Coba lagi dalam {i+1:02d} detik", end="\r")
    time.sleep(1)
    