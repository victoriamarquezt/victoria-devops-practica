# Tienda Online – DevOps Práctica

**Autor:** Victoria Márquez 

## Descripción del proyecto

Este repositorio contiene el desarrollo de una aplicación Python basada en los contenidos de la Práctica 1.3.  
El objetivo del proyecto es implementar una primera versión de una **tienda online** utilizando programación orientada a objetos en Python.  

La aplicación incluye:

- Gestión de productos mediante clases y subclases (producto base, electrónicos, ropa).
- Gestión de usuarios (clientes y administradores).
- Creación y manejo de pedidos con actualización automática de stock.
- Un servicio central `TiendaService` que coordina las operaciones clave.
- Un archivo `main.py` que actúa como punto de entrada para probar el sistema.
Actualización 2.2

a) Cómo construir la imagen:
Para construir la imagen Docker debes situarte en la carpeta raíz del proyecto y ejecutar el comando:
docker build -t tienda_online:1.0 .
Este comando crea una imagen llamada “tienda_online” con la etiqueta “1.0”.

b) Cómo ejecutarla (incluye ejemplos de docker run):
Una vez construida la imagen, puedes ejecutar la aplicación con el siguiente comando:
docker run --rm tienda_online:1.0
Al hacerlo, Docker iniciará un contenedor y ejecutará automáticamente el archivo main.py dentro de la imagen. El contenedor se eliminará al terminar gracias a la opción --rm.

c) Variables de entorno soportadas (si aplica):
En esta versión de la aplicación no se utilizan variables de entorno. No es necesario configurar nada externo para ejecutar el contenedor.

d) Salida esperada o pasos de prueba:
Al ejecutar el contenedor deberías ver en la terminal:
– La creación de varios productos de ejemplo.
– La creación de usuarios (clientes y administrador).
– La realización de pedidos utilizando TiendaService.
– La actualización del stock de los productos.
– El cálculo del importe total del pedido y un resumen final.

Esta salida confirma que la aplicación funciona correctamente dentro del contenedor Docker.




