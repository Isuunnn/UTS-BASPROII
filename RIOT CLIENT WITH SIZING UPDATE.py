import tkinter as tk
from tkinter import messagebox

# Simulasi data update dari game-game Riot
game_updates = {
    "League of Legends": {
        "update_available": True,
        "version": "14.8",
        "size": "1.2 GB"
    },
    "Teamfight Tactics": {
        "update_available": False,
        "version": "7.12",
        "size": "0 GB"
    },
    "Valorant": {
        "update_available": True,
        "version": "14.8b",
        "size": "2.7 GB"
    },
    "Legends of Runeterra": {
        "update_available": False,
        "version": "5.6",
        "size": "0 GB"
    }
}

# Fungsi untuk menampilkan notifikasi update
def check_updates():
    updates = []
    for game, info in game_updates.items():
        if info["update_available"]:
            updates.append(f"{game} - Update {info['version']} tersedia ({info['size']})")

    if updates:
        messagebox.showinfo("Update Tersedia", "\n".join(updates))
    else:
        messagebox.showinfo("Update Tersedia", "Semua game sudah versi terbaru!")

# Membuat GUI utama
root = tk.Tk()
root.title("Riot Client - Python Version")
root.geometry("400x300")
root.configure(bg="#1a1a1a")

# Label judul
title = tk.Label(root, text="Riot Game Client", font=("Helvetica", 18, "bold"), fg="white", bg="#1a1a1a")
title.pack(pady=20)

# Tombol untuk mengecek update
check_button = tk.Button(root, text="Cek Update Game", command=check_updates, bg="#e63946", fg="white", font=("Helvetica", 12, "bold"))
check_button.pack(pady=10)

# Daftar game dan status
for game, info in game_updates.items():
    status = "✅ Terbaru" if not info["update_available"] else f"⬆️ Update ke {info['version']}"
    label = tk.Label(root, text=f"{game}: {status}", fg="white", bg="#1a1a1a", font=("Helvetica", 11))
    label.pack()

# Jalankan GUI
root.mainloop()
