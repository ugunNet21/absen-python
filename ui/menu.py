import tkinter as tk
from auth.admin_data import ADMIN_CREDENTIALS
from ui.kepala_sekolah import KepalaSekolahPage
from ui.siswa import SiswaPage
from ui.guru import GuruPage
import sys
import os

class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        self.create_login_ui()

    def create_login_ui(self):
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Label(self, text="Username:").pack()
        tk.Entry(self, textvariable=self.username_var).pack()

        tk.Label(self, text="Password:").pack()
        tk.Entry(self, textvariable=self.password_var, show="*").pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=5)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username] == password:
            self.show_admin_menu()
        else:
            tk.messagebox.showerror("Login Gagal", "Username atau Password salah.")

    def show_admin_menu(self):
        self.destroy()

        tk.Label(self.parent, text="Selamat datang, Admin!", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.parent, text="Kepala Sekolah", command=self.show_kepala_sekolah_page).pack(pady=5)
        tk.Button(self.parent, text="Siswa", command=self.show_siswa_page).pack(pady=5)
        tk.Button(self.parent, text="Guru", command=self.show_guru_page).pack(pady=5)

    def show_kepala_sekolah_page(self):
        self.destroy()
        KepalaSekolahPage(self.parent)

    def show_siswa_page(self):
        self.destroy()
        SiswaPage(self.parent)

    def show_guru_page(self):
        self.destroy()
        GuruPage(self.parent)
