# Aplicación GUI: To-Do List Interactiva (Mejorada)

Aplicación de escritorio para la gestión de tareas diarias, desarrollada en Python utilizando `Tkinter`. 

Esta versión  mantiene estrictamente la **Arquitectura por Capas** (Modelos, Servicios, UI) e introduce un manejo avanzado de **Eventos de Teclado y Ratón** para optimizar la interacción del usuario.

## 🚀 Características Principales

1. **Arquitectura Limpia:** Separación total entre la lógica de negocio y la interfaz gráfica.
2. **Feedback Visual:** Las tareas completadas cambian automáticamente su diseño (se vuelven grises y su texto aparece tachado) gracias a los `tags` del Treeview.
3. **Interacción Dual:** Todas las acciones se pueden realizar haciendo clic en los botones o utilizando atajos de teclado globales.

### ⌨️ Atajos de Teclado Implementados (`.bind`)
- `[Enter]`: Añade la tarea escrita en el cuadro de texto.
- `[Doble Clic Izquierdo]`: Sobre una tarea en la lista, la marca como completada.
- `[C]`: Marca la tarea seleccionada como completada (Validado para no interferir si se está escribiendo en el campo de texto).
- `[D]` o `[Supr/Delete]`: Elimina permanentemente la tarea seleccionada.
- `[Esc]`: Cierra la aplicación.

## 📁 Estructura del Proyecto

* **`modelos/tarea.py`:** Define la entidad y sus atributos.
* **`servicios/tarea_servicio.py`:** Contiene la lógica del negocio.
* **`ui/app_tkinter.py`:** Administra exclusivamente el diseño y la captura de eventos.
* **`main.py`:** Orquesta el sistema instanciando el servicio y enviándolo a la UI.

## 🛠️ Cómo Ejecutar
1. Abre tu terminal en la carpeta principal.
2. Ejecuta:
   ```bash
   python main.py