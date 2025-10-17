from services.Tienda_service import TiendaService
from models.Producto import ProductoElectronico, ProductoRopa
from models.Usuario import Cliente, Administrador

""" Crear instancia del servicio de la tienda"""
tienda = TiendaService()

""" Registrar usuarios: 3 clientes y 1 administrador"""
c1 = tienda.registro_usuarios("cliente", "Xavier",   "Xavier@gmail.com",  "Gran Vía 2")
c2 = tienda.registro_usuarios("cliente", "Coco",     "coquito@gmail.com", "Ramon Nieto 400")
c3 = tienda.registro_usuarios("cliente", "Vera",     "vera@gmail.com",    "Hernán Cortes 6")
admin = tienda.registro_usuarios("administrador", "Victoria", "victoria@gmail.com")

""" Crear y añadir productos al inventario"""
p1 = ProductoElectronico("Kindle",     95.00, 20, 12)
p2 = ProductoElectronico("iPhone 17", 1250.0, 30, 12)
p3 = ProductoRopa       ("Vestido",    300.0, 50, "M", "Rosa")
p4 = ProductoRopa       ("Pantalón",   100.0, 30, "L", "Negro")
p5 = ProductoElectronico("iPad",       499.0, 10, 24)

for p in (p1, p2, p3, p4, p5):
    tienda.agregar_producto(p)

print("\n Inventario inicial ")
for prod in tienda.listar_productos():
    print(prod)

"""3 pedidos (cada item es (id_producto, cantidad))"""
pedido1 = tienda.realizar_pedido(c1.id, [(p1.id, 2), (p3.id, 1)])
pedido2 = tienda.realizar_pedido(c2.id, [(p2.id, 1), (p4.id, 2)])
pedido3 = tienda.realizar_pedido(c3.id, [(p5.id, 1), (p3.id, 3)])

print("\n Pedidos realizados ")
for ped in (pedido1, pedido2, pedido3):
    print(ped)

print(f"\n Histórico de pedidos de {c1.nombre} ")
for ped in tienda.listar_pedidos_usuario(c1.id):
    print(ped)

print("\n--- Inventario tras pedidos ---")
for prod in tienda.listar_productos():
    print(prod)
