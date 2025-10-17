from models.Usuario import Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido

class TiendaService:
    """ Servicio que centraliza operaciones de la tienda, nos piden que:
    - Registremos usuarios (cliente/administrador)
    - Añadir / eliminar / listar productos
    - Realialicemos pedidos (valida usuario y stock) y listar pedidos de un usuario"""
    def __init__(self):
        self.usuarios: dict[str, Cliente | Administrador] = {}  # id -> Usuario
        self.productos: dict[str, Producto] = {}                # id -> Producto
        self.pedidos: list[Pedido] = []                         # pedidos


# Usuarios 
    def registro_usuarios(self, tipo: str, nombre: str, email: str, direccion: str = None):
        """ Creamos usuarios y los clasificamos según su tipo (cliente o administrador), comprobando si en cliente tiene la dirreción postal.
        Si el tipo de usuario no es ni cliente ni administrador, manda mensaje: no valido;
        En caso de que sea el tipo correcto evuelve el usuario creado """
        t = tipo.lower()
        if t == "cliente":
            if not direccion:
                raise ValueError("El cliente requiere 'direccion'")
            u = Cliente(nombre, email, direccion) #siendo u el objeto que se crea 
        elif t == "administrador":
            u = Administrador(nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido (usa 'cliente' o 'administrador')")

        self.usuarios[u.id] = u #Guarda al usuario u en el diccionario usuarios, usando su id  como clave (get)
        return u

#Productos
    def agregar_producto(self, producto: Producto) -> None:
        """Añade el objeto producto al inventario (self.productos), usando como clave el id del producto"""
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> Producto:
        """Si el producto no está en el inventario (productos), mensaje de error"""
        if producto_id not in self.productos:
            raise ValueError("Producto no encontrado.")
        return self.productos.pop(producto_id) # quita  del inventario el id y devuelve el valor en caso de que lo querramos recuperar 

    def listar_productos(self) -> list:
        """Devuelve la lista de productos disponibles"""
        return list(self.productos.values())

#Pedidos 
    def realizar_pedido(self, id_usuario: str, items) -> Pedido:
        """ Crea un pedido si el usuario existe (y es Cliente) y hay stock suficiente
        items: producto_id, cantidad  """
        #comprobamos usuario 
        usuario = self.usuarios.get(id_usuario)
        if usuario is None:
            raise ValueError("El usuario no existe.") #verificando que el usuario que lo solicita existe
        if not isinstance(usuario, Cliente):   #isinstance devuelve true o false 
            raise ValueError("Solo un Cliente puede realizar pedidos.") # solo los  clientes hacen pedidos
        # Verificamos stock 
        lineas = [] #creo lista vacia para guardar productos y cantidad 
        for prod_id, cant in items:
            prod = self.productos.get(prod_id) #busqueda en inventario con el id 
            if prod is None:
                raise ValueError(f"Producto {prod_id} no existe.")
            if not prod.comprobar_stock(cant):
                raise ValueError(
                    f"Stock insuficiente de '{prod.nombre}'. "
                    f"Disponible: {prod.stock}, pedido: {cant}."
                )
            lineas.append((prod, cant)) #en caso de que exista lo añadimos a lineas 
       
        """ Descontamos la cantidad del producto pedido al stock y atualizamos pedido con usuario y producto-cantidad (lista) """

        # Descontar stock (ya verificado)
        for prod, cant in lineas:
            prod.actualizar_stock(-cant)
        

        pedido = Pedido(usuario, lineas)
        self.pedidos.append(pedido)
        return pedido
    

    # Ordenar por fecha 
    def listar_pedidos_usuario(self, id_usuario: str) -> list:
        """Devuelve los pedidos del usuario ordenados por fecha (más recientes primero)."""
        return sorted(
            (p for p in self.pedidos if p.cliente.id == id_usuario), #selecciona solo los pedidos de ese  cliente 
            key=lambda p: p.fecha, # clave de la ordenación: lambda- por fecha de peidido 
            reverse=True
        )

