import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppListaTareas

def main():
    root = tk.Tk()
    servicio = TareaServicio()
    app = AppListaTareas(root, servicio)
    root.mainloop()

if __name__ == "__main__":
    main()