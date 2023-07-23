import cv2
from detection.face_detection import face_detection
import tkinter as tk

class KepalaSekolahPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        tk.Label(self, text="Halaman Absensi Kepala Sekolah", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self, text="Absen", command=self.absen).pack(pady=5)
        tk.Button(self, text="Kembali", command=self.go_back).pack(pady=5)

    def absen(self):
        # Implementasi deteksi wajah dan logika absensi disini
        # Panggil fungsi face_detection untuk mendeteksi wajah
        image_path = "path/to/image.jpg"  # Ganti dengan path gambar yang ingin diuji
        result = face_detection(image_path)  # Hasil deteksi wajah (True/False)

        if result:
            tk.messagebox.showinfo("Absensi Berhasil", "Anda berhasil melakukan absensi.")
        else:
            tk.messagebox.showwarning("Absensi Gagal", "Wajah tidak terdeteksi atau tidak cocok.")

    def go_back(self):
        self.destroy()
        MainMenu(self.parent)
