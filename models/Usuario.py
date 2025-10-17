from uuid import uuid4


class Usuario:
    """Atributos de la clase base   Usuario:
        id (str): UUIDv4, genera  un identificador de 128 bits, probabilidades casi 0 que se repita
        nombre (str)
        email(str)"""

    def __init__(self, nombre: str, email: str) -> None:
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.email: str = email
    
    def is_admin(self) -> bool:
        """Indica si el usuario es administrador (por defecto False)"""
        return False

class Cliente (Usuario):
    """Subclase de Usuario para clientes, con el  atributo adicional (super): dirección postal """
    def __init__(self, nombre: str, email: str, direccion: str) -> None:
        super().__init__(nombre, email)
        self.direccion: str = direccion

class Administrador (Usuario): 
   """Subclase de Usuario para administrador devuelve True si en caso de ser admin """
   def is_admin(self) -> bool:
      return True 



    