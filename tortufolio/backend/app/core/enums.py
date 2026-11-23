import enum


class RolUsuario(str, enum.Enum):
    """
    Roles del sistema (RS-13).
    Hereda de 'str' para que al serializar a JSON salga "admin"
    en vez de 'RolUsuario.admin'.
    - admin: gestiona usuarios y toda la plataforma
    - gestor: gestiona proyectos y documentos (trabajadores DIT)
    - visualizador: ve proyectos asignados, recibe newsletter
    """
    admin = "admin"
    gestor = "gestor"
    visualizador = "visualizador"


class Facultad(str, enum.Enum):
    """
    Facultades válidas de la universidad.
    Mismo patrón: hereda de 'str' + 'enum.Enum'.
    Los nombres (izquierda) son las claves internas de Python.
    Los valores (derecha) son lo que se guarda en la BD y se muestra en JSON.
    """
    ciencias_sociales = "Ciencias Sociales"
    economia_y_negocios = "Economia y Negocios"
    educacion = "Educación"
    filosofia_y_humanidades = "Filosofía y Humanidades"
    ingenieria = "Ingenieria"
    derecho = "Derecho"
