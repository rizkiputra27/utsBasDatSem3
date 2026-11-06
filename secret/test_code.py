from winotify import Notification, audio
import time
import questionary
import os
import dialite


# notif1 = Notification(
#                 app_id = "Informasi Akun",
#                 title = "Akun anda telah terblokir",
#                 msg = "Hubungi akun untuk membuka kembali",
#                 duration = "short"
#             )
# notif1.set_audio(audio.Default, loop=False)
# notif1.show()
# stop = 10
# for i in range(stop):
#     print(f"Coba lagi dalam {i+1:02d} detik", end="\r")
#     time.sleep(1)



# from prettytable import PrettyTable

# # 1. Buat tabel dengan PrettyTable
# struk = PrettyTable()
# struk.field_names = ["Barang", "Qty", "Total"]
# struk.align["Barang"] = "L"
# struk.align["Qty"] = "C"
# struk.align["Total"] = "R"

# struk.add_row(["Kopi Susu", "2", "36.000"])
# struk.add_row(["Roti Bakar", "1", "15.000"])

# # 2. Desain layout struk teks
# isi_struk = f"""
#      TOKO BERKAH JAYA
#   Jl. Nusantara No. 123
# ==========================
# {struk}
# ==========================
# Total Belanja: Rp 51.000
# Bayar        : Rp 60.000
# Kembali      : Rp  9.000
# ==========================
#    Terima Kasih Banyak
# """

# # 3. Simpan isi struk menjadi file .txt
# nama_file = "struk_sementara.txt"
# with open(nama_file, "w") as file:
#     file.write(isi_struk)

# # 4. Cetak file teks langsung ke printer default Windows
# os.startfile(nama_file, "print")
dialite.inform("Informasi","Berhasil di simpan ke Database")
