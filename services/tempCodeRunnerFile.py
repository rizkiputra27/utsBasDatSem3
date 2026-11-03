def tampil_menu():
        menu_admin = questionary.rawselect(
            "===== MENU ADMIN =====",
            choices = [
                Choice(title = "Kelola Produk", value = "1"),
                Choice(title = "Kelola Stok", value = "2"),
                Choice(title = "Kelola Kasir", value = "3"),
            ]
        ).ask()