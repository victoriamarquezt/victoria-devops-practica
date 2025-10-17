
from datetime import datetime
from models.Producto import Producto
from models.Usuario import Cliente
from uuid import uuid4




class Pedido:
    """
    Atributos de la clase base Pedido:
        id (str): Identificador (UUIDv4).
        fecha (datetime)
        productos: Colección de productos con sus cantidades """

    def __init__(self, cliente: Cliente, productos) -> None:
        self.id: str = str(uuid4())
        self.fecha: datetime = datetime.now()
        self.cliente: Cliente = cliente
        self.productos = productos  
        """Lista de tuplas (producto, cantidad)""" 

    def total_compra(self) -> float:
        """Calcula el importe total de la compra"""
        total = 0.0
        for prod, cant in self.productos:
            total += prod.precio * cant
        return total

    def __str__(self) -> str:
        """Devuelve el texto  del pedido"""
        items = ", ".join(f"{prod.nombre} x{cant}" for prod, cant in self.productos)
        return (
            f"Pedido {self.id} - Cliente: {self.cliente.nombre} - "
            f"Items: {items} - Total: {self.total_compra():.2f} €"
        )
