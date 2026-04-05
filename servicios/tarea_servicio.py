from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.__tareas = {}
        self.__contador_id = 1  # Simulo un ID autoincremental

    def agregar_tarea(self, descripcion: str):
        if not descripcion.strip():
            return False, "La descripción no puede estar vacía."
        
        nueva_tarea = Tarea(self.__contador_id, descripcion)
        self.__tareas[self.__contador_id] = nueva_tarea
        self.__contador_id += 1
        return True, "Tarea agregada."

    def completar_tarea(self, id_tarea: int):
        if id_tarea in self.__tareas:
            self.__tareas[id_tarea].marcar_completada()
            return True, "Tarea completada."
        return False, "Tarea no encontrada."

    def eliminar_tarea(self, id_tarea: int):
        if id_tarea in self.__tareas:
            del self.__tareas[id_tarea]
            return True, "Tarea eliminada."
        return False, "Tarea no encontrada."

    def obtener_todas(self):
        # Retorna la lista de objetos Tarea
        return list(self.__tareas.values())