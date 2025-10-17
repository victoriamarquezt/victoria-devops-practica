from uuid import uuid4
class Producto:
    """Atributos de la clase base Producto:
        id (str): UUIDv4, genera  un identificador de 128 bits, probabilidades casi 0 que se repita
        nombre (str)
        precio (float)
        stock (int): Unidades disponibles en inventario"""
    
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
       
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.precio: float = float(precio)
        self.stock: int = int(stock)
    
    def comprobar_stock(self, cantidad: int) -> bool:
        """ verifica que hay suficiente stock para pedir x cantidad (stock>cantidad) y tiene en cuenta que la cantidad nunca va a ser negativa"""
        return cantidad >= 0 and self.stock >= cantidad
    
    def actualizar_stock(self, cantidad: int) -> None: 
        """Modifica el número de unidades de stock y comprueba la cantidad de stock """  #a pesar de que se ha comprobado en el comprobar, lo hago por si se llama directamente a actualizar 
        nuevo_stock = self.stock + cantidad
        if nuevo_stock < 0:
            raise ValueError(f"Stock insuficiente de '{self.nombre}' (disponible {self.stock})")
        self.stock = nuevo_stock

    def __str__(self) -> str:
        """Texto de las características principales del producto"""
        return (f"ID: {self.id} | Nombre: {self.nombre} | Precio: {self.precio:.2f}€ | Stock: {self.stock}")


class ProductoElectronico(Producto):
   """Subclase de Producto para artículos electrónicos, añadimos atributo adicional de garantía (super)"""
  
   def __init__(self, nombre: str, precio: float, stock: int, garantia: int) -> None:
        super().__init__(nombre, precio, stock)
        self.garantia: int = garantia
    

   def __str__(self):
     return (
     f"ID: {self.id} | Nombre: {self.nombre} | Precio: {self.precio:2f}€ | Stock: {self.stock} | Garantía: {self.garantia}")


class ProductoRopa(Producto):
    """Subclase de Producto para ropa, añadimos atributos adicionales talla y color (super)"""
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Precio: {self.precio:2f}€ | Stock: {self.stock} | Talla: {self.talla}| Color: {self.color}")



    