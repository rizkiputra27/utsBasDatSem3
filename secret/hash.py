import bcrypt

# Password administrator
password = "tibd2a"

# Ubah password menjadi bytes
password_bytes = password.encode("utf-8")

# Buat hash bcrypt
hashed = bcrypt.hashpw(
    password_bytes,
    bcrypt.gensalt(rounds=12)
)

# Tampilkan hasil hash
print(hashed.decode("utf-8"))
