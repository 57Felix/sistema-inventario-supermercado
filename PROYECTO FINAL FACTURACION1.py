import os

# Directorio donde se guardarán los archivos
base_dir = "C:\\Archivos\\Grupo7"

# Inicializar diccionarios para almacenar datos
usuarios = {"Admin": "Algoritmos123"}
clientes = {}
productos = {}
categorias = {}
facturas = []

# Función para guardar datos en archivos
def guardar_datos(datos, archivo):
    with open(os.path.join(base_dir, archivo), "w") as file:
        for clave, valor in datos.items():
            file.write(f"{clave}: {valor}\n")

# Función para cargar datos desde archivos
def cargar_datos(archivo):
    datos = {}
    with open(os.path.join(base_dir, archivo), "r") as file:
        for linea in file:
            clave, valor = linea.strip().split(": ")
            datos[clave] = valor
    return datos

# Función para validar el ingreso al sistema
def validar_ingreso():
    while True:
        nombre_usuario = input("Usuario: ")
        password = input("Contraseña: ")
        
        if nombre_usuario in usuarios and usuarios[nombre_usuario] == password:
            print("Acceso concedido. ¡Bienvenido!")
            return nombre_usuario
        else:
            print("Credenciales incorrectas. Intente de nuevo.")


    if __name__ == "__main__":
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

     # Validar el ingreso al sistema
    usuario_actual = validar_ingreso()

     # Cargar datos de archivos si existen
    if os.path.exists(os.path.join(base_dir, "Usuarios.txt")):
        usuarios = cargar_datos("Usuarios.txt")

    print("Supermercado 'EL ARABE'")
    print("5 AVENIDA 8-9 El Triangulo zona 9")
    print("Telefono: 24201112")

    # Validar el ingreso al sistema
    usuario_actual = validar_ingreso()

    # El usuario actual es "Admin" 



# Función para el menú principal
def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Usuarios")
        print("2. Clientes")
        print("3. Productos")
        print("4. Categoría de Productos")
        print("5. Facturación")
        print("6. Salida del Sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_productos()
        elif opcion == "4":
            menu_categorias()
        elif opcion == "5":
            menu_facturacion()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Funciones para el módulo de Usuarios
def menu_usuarios():
    while True:
        print("\nMódulo de Usuarios")
        print("1. Alta Usuario")
        print("2. Baja Usuario")
        print("3. Modificación Usuario")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_usuario()
        elif opcion == "2":
            baja_usuario()
        elif opcion == "3":
            modificacion_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def alta_usuario():
    nombre = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    usuarios[nombre] = password
    print("Usuario dado de alta con éxito.")
    guardar_datos(usuarios, "Usuarios.txt")

def baja_usuario():
    nombre = input("Ingrese el nombre de usuario a dar de baja: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario dado de baja con éxito.")
        guardar_datos(usuarios, "Usuarios.txt")
    else:
        print("Usuario no encontrado.")

def modificacion_usuario():
    nombre = input("Ingrese el nombre de usuario a modificar: ")
    if nombre in usuarios:
        password = input("Ingrese la nueva contraseña: ")
        usuarios[nombre] = password
        print("Usuario modificado con éxito.")
        guardar_datos(usuarios, "Usuarios.txt")
    else:
        print("Usuario no encontrado.")

# Funciones para el módulo de Clientes
def menu_clientes():
    while True:
        print("\nMódulo de Clientes")
        print("1. Alta Cliente")
        print("2. Baja Cliente")
        print("3. Modificación Cliente")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_cliente()
        elif opcion == "2":
            baja_cliente()
        elif opcion == "3":
            modificacion_cliente()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def alta_cliente():
    codigo = input("Ingrese el código del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")

    cliente = {
        "Codigo": codigo,
        "Nombre": nombre,
        "Direccion": direccion,
        "Telefono": telefono,
        "Nit": nit
    }

    clientes[codigo] = cliente
    print("Cliente dado de alta con éxito.")
    guardar_datos(clientes, "Clientes.txt")

def baja_cliente():
    codigo = input("Ingrese el código del cliente a dar de baja: ")
    if codigo in clientes:
        del clientes[codigo]
        print("Cliente dado de baja con éxito.")
        guardar_datos(clientes, "Clientes.txt")
    else:
        print("Cliente no encontrado.")

def modificacion_cliente():
    codigo = input("Ingrese el código del cliente a modificar: ")
    if codigo in clientes:
        cliente = clientes[codigo]
        print("\nRegistro de clientes")
        print(f"Codigo: {cliente['Codigo']}")
        print(f"Nombre: {cliente['Nombre']}")
        print(f"Direccion: {cliente['Direccion']}")
        print(f"Telefono: {cliente['Telefono']}")
        print(f"Nit: {cliente['Nit']}\n")

        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
        nuevo_direccion = input("Ingrese la nueva dirección del cliente: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono del cliente: ")
        nuevo_nit = input("Ingrese el nuevo NIT del cliente: ")

        cliente["Nombre"] = nuevo_nombre
        cliente["Direccion"] = nuevo_direccion
        cliente["Telefono"] = nuevo_telefono
        cliente["Nit"] = nuevo_nit

        print("Cliente modificado con éxito.")
        guardar_datos(clientes, "Clientes.txt")
    else:
        print("Cliente no encontrado.")

# Funciones para el módulo de Productos
def menu_productos():
    while True:
        print("\nMódulo de Productos")
        print("1. Alta Producto")
        print("2. Modificación de Producto (Cantidad Inventario)")
        print("3. Consulta de inventario (por código de producto)")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_producto()
        elif opcion == "2":
            modificacion_producto()
        elif opcion == "3":
            consulta_inventario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def alta_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad en inventario del producto: ")

    producto = {
        "Codigo": codigo,
        "Nombre": nombre,
        "Descripcion": descripcion,
        "Precio": precio,
        "Cantidad": cantidad
    }

    productos[codigo] = producto
    print("Producto dado de alta con éxito.")
    guardar_datos(productos, "Productos.txt")

def modificacion_producto():
    codigo = input("Ingrese el código del producto a modificar: ")
    if codigo in productos:
        producto = productos[codigo]
        print("\nRegistro de productos")
        print(f"Codigo: {producto['Codigo']}")
        print(f"Nombre: {producto['Nombre']}")
        print(f"Descripcion: {producto['Descripcion']}")
        print(f"Precio: {producto['Precio']}")
        print(f"Cantidad: {producto['Cantidad']}\n")

        nueva_cantidad = input("Ingrese la nueva cantidad en inventario del producto: ")
        producto["Cantidad"] = nueva_cantidad

        print("Producto modificado con éxito.")
        guardar_datos(productos, "Productos.txt")
    else:
        print("Producto no encontrado.")

def consulta_inventario():
    codigo = input("Ingrese el código del producto a consultar: ")
    if codigo in productos:
        producto = productos[codigo]
        print("\nRegistro de productos")
        print(f"Codigo: {producto['Codigo']}")
        print(f"Nombre: {producto['Nombre']}")
        print(f"Descripcion: {producto['Descripcion']}")
        print(f"Precio: {producto['Precio']}")
        print(f"Cantidad: {producto['Cantidad']}\n")
    else:
        print("Producto no encontrado.")

# Funciones para el módulo de Categoría de Productos
def menu_categorias():
    while True:
        print("\nMódulo de Categoría de Productos")
        print("1. Alta de Categoría")
        print("2. Baja de Categoría")
        print("3. Reporte de productos por Categoría")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_categoria()
        elif opcion == "2":
            baja_categoria()
        elif opcion == "3":
            reporte_categorias()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def alta_categoria():
    codigo = input("Ingrese el código de la categoría: ")
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")

    categoria = {
        "Codigo": codigo,
        "Nombre": nombre,
        "Descripcion": descripcion
    }

    categorias[codigo] = categoria
    print("Categoría dada de alta con éxito.")
    guardar_datos(categorias, "Categorias.txt")

def baja_categoria():
    codigo = input("Ingrese el código de la categoría a dar de baja: ")
    if codigo in categorias:
        del categorias[codigo]
        print("Categoría dada de baja con éxito.")
        guardar_datos(categorias, "Categorias.txt")
    else:
        print("Categoría no encontrada.")

def reporte_categorias():
    print("\nRegistro de Categoría de producto")
    for codigo, categoria in categorias.items():
        print("Código:", categoria["Codigo"])
        print("Nombre:", categoria["Nombre"])
        print("Descripción:", categoria["Descripcion"])
        print()

# Funciones para el módulo de Facturación
def menu_facturacion():
    while True:
        print("\nMódulo de Facturación")
        print("1. Facturar (Al facturar debe bajar la cantidad de productos)")
        print("2. Buscar Factura")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            facturar()
        elif opcion == "2":
            buscar_factura()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def facturar():
    print("\nSupermercado 'EL ARABE'")
    print("5 AVENIDA 8-9 El Triangulo zona 9")
    print("Telefono: 24201112")
    print()
    print("Ingrese los datos de la factura:")
    nombre_cliente = input("Nombre del cliente: ")
    nit_cliente = input("Nit del cliente: ")
    direccion_cliente = input("Dirección del cliente: ")
    fecha = input("Fecha (dd/mm/yyyy): ")

    factura = {
        "Nombre": nombre_cliente,
        "Nit": nit_cliente,
        "Direccion": direccion_cliente,
        "Fecha": fecha,
        "Productos": []
    }

    while True:
        codigo_producto = input("Código del producto (0 para finalizar): ")
        if codigo_producto == "0":
            break
        if codigo_producto in productos:
            cantidad = int(input(f"Cantidad de '{productos[codigo_producto]['Nombre']}': "))
            if cantidad <= int(productos[codigo_producto]["Cantidad"]):
                productos[codigo_producto]["Cantidad"] = str(int(productos[codigo_producto]["Cantidad"]) - cantidad)
                factura["Productos"].append({
                    "Codigo": codigo_producto,
                    "Descripcion": productos[codigo_producto]["Nombre"],
                    "Precio Unitario": productos[codigo_producto]["Precio"],
                    "Cantidad": cantidad,
                    "Total": float(productos[codigo_producto]["Precio"]) * cantidad
                })
            else:
                print("No hay suficiente stock de este producto.")
        else:
            print("Código de producto no válido.")

    total_factura = sum(item["Total"] for item in factura["Productos"])
    factura["Total"] = total_factura
    facturas.append(factura)

    print("\nFactura generada con éxito.")
    guardar_datos(productos, "Productos.txt")

def buscar_factura():
    factura_numero = input("Ingrese el número de factura a buscar: ")
    if factura_numero.isdigit() and int(factura_numero) > 0 and int(factura_numero) <= len(facturas):
        factura = facturas[int(factura_numero) - 1]
        print("\nSupermercado 'EL ARABE'")
        print("5 AVENIDA 8-9 El Triangulo zona 9")
        print("Telefono: 24201112")
        print()
        print(f"FACTURA No. {factura_numero}")
        print()
        print(f"Nombre: {factura['Nombre']}               Nit: {factura['Nit']}")
        print(f"Direccion: {factura['Direccion']}")
        print()
        print("Cantidad    Cod Producto       Descripción        Precio Unitario    Total")
        print("-------------------------------------------------------------------------")
        for i, producto in enumerate(factura["Productos"], start=1):
            print(f"  {i}         {producto['Codigo']}                   {producto['Descripcion']}"
                  f"        {producto['Precio Unitario']}             {producto['Total']:.2f}")
        print()
        print("TOTAL                                            ", factura["Total"])
    else:
        print("Factura no encontrada.")

if __name__ == "__main__":
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Cargar datos de archivos si existen
    if os.path.exists(os.path.join(base_dir, "Usuarios.txt")):
        usuarios = cargar_datos("Usuarios.txt")
    if os.path.exists(os.path.join(base_dir, "Clientes.txt")):
        clientes = cargar_datos("Clientes.txt")
    if os.path.exists(os.path.join(base_dir, "Productos.txt")):
        productos = cargar_datos("Productos.txt")
    if os.path.exists(os.path.join(base_dir, "Categorias.txt")):
        categorias = cargar_datos("Categorias.txt")

    menu_principal()
