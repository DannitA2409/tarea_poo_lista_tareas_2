import tkinter as tk
from tkinter import ttk, messagebox

class AppListaTareas:
    def __init__(self, root, servicio):
        self.root = root
        self.root.title("To-Do List Interactiva (Con Atajos)") 
        self.root.geometry("550x480") 
        self.servicio = servicio

        self._crear_interfaz()
        self._configurar_eventos()
        self.actualizar_lista()

    def _crear_interfaz(self):
        # Entrada de datos
        frame_top = tk.Frame(self.root, pady=10)
        frame_top.pack(fill="x", padx=10)

        tk.Label(frame_top, text="Nueva Tarea:").pack(side="left")
        self.entry_desc = tk.Entry(frame_top, width=35)
        self.entry_desc.pack(side="left", padx=5)
        
        self.btn_add = tk.Button(frame_top, text="Añadir", bg="#4CAF50", fg="white", command=self.evento_agregar)
        self.btn_add.pack(side="left")

        # Texto de ayuda visual para enseñar los atajos al usuario
        texto_atajos = "ATAJOS: [Enter] Añadir | [C] Completar | [D] o [Supr] Eliminar | [Esc] Salir"
        tk.Label(self.root, text=texto_atajos, fg="gray", font=("Arial", 8, "italic")).pack(pady=2)

        # Treeview
        frame_mid = tk.Frame(self.root)
        frame_mid.pack(fill="both", expand=True, padx=10, pady=5)

        columnas = ("id", "descripcion", "estado")
        self.tree = ttk.Treeview(frame_mid, columns=columnas, show="headings", selectmode="browse")
        self.tree.heading("id", text="ID")
        self.tree.heading("descripcion", text="Descripción de la Tarea")
        self.tree.heading("estado", text="Estado")

        self.tree.column("id", width=30, anchor="center")
        self.tree.column("descripcion", width=300, anchor="w")
        self.tree.column("estado", width=100, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # Se añadió 'tachado' a las tareas completadas
        self.tree.tag_configure("pendiente", foreground="black")
        self.tree.tag_configure("completada", foreground="gray", font=("Arial", 9, "italic", "overstrike"))

        # Botones de Acción
        frame_bot = tk.Frame(self.root, pady=10)
        frame_bot.pack(fill="x")

        tk.Button(frame_bot, text="✔ Marcar Completada (C)", bg="#2196F3", fg="white", command=self.evento_completar).pack(side="left", padx=20, expand=True)
        tk.Button(frame_bot, text="🗑 Eliminar (D / Supr)", bg="#f44336", fg="white", command=self.evento_eliminar).pack(side="right", padx=20, expand=True)

    def _configurar_eventos(self):
        """ EVENTOS DE TECLADO Y RATÓN """
        self.entry_desc.bind("<Return>", self.evento_agregar)
        self.tree.bind("<Double-1>", self.evento_completar)

    # MÉTODOS DE EVENTOS
    def evento_agregar(self, event=None):
        desc = self.entry_desc.get()
        exito, msj = self.servicio.agregar_tarea(desc)
        if exito:
            self.entry_desc.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", msj)

    def evento_completar(self, event=None):
        seleccion = self.tree.selection()
        if not seleccion:
            if not event: 
                messagebox.showwarning("Aviso", "Seleccione una tarea para completarla.")
            return

        item = self.tree.item(seleccion[0])
        id_tarea = int(item['values'][0])
        self.servicio.completar_tarea(id_tarea)
        self.actualizar_lista()

    def evento_eliminar(self, event=None):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione una tarea para eliminarla.")
            return

        item = self.tree.item(seleccion[0])
        id_tarea = int(item['values'][0])
        self.servicio.eliminar_tarea(id_tarea)
        self.actualizar_lista()

    def actualizar_lista(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
            
        for t in self.servicio.obtener_todas():
            estado_texto = "✔ [Hecho]" if t.estado_completado else "Pendiente"
            tag = "completada" if t.estado_completado else "pendiente"
            self.tree.insert("", tk.END, values=(t.id, t.descripcion, estado_texto), tags=(tag,))