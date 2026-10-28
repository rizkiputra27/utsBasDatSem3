import mysql.connector

def get_conection():
    try:
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "kasir"
        )
        return db
    except mysql.connector.Error as err:
        print(f" ❌ Error koneksi: {err}")

        return None