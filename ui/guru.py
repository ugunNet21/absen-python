import tkinter as tk

class GuruPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        tk.Label(self, text="Halaman Absensi Guru", font=("Helvetica", 14)).pack(pady=10)
        # Implementasi tampilan input absensi dan deteksi wajah (bisa menggunakan OpenCV).

        tk.Button(self, text="Kembali", command=self.go_back).pack(pady=5)

    def go_back(self):
        self.destroy()
        MainMenu(self.parent)
