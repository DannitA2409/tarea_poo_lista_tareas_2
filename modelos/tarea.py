class Tarea:
    def __init__(self, id_tarea: int, descripcion: str):
        self.__id = id_tarea
        self.__descripcion = descripcion
        self.__estado_completado = False  # Por defecto, una tarea nace pendiente

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def estado_completado(self):
        return self.__estado_completado

    # Setter para cambiar el estado
    def marcar_completada(self):
        self.__estado_completado = True