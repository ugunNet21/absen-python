import tkinter as tk
from ui.menu import MainMenu

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplikasi Absensi")
    main_menu = MainMenu(root)
    root.mainloop()
