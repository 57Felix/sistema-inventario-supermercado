import os
import tkinter as tk
from tkinter import messagebox

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
    nombre_usuario = entry_usuario.get()
    password = entry_password.get()

    if nombre_usuario in usuarios and usuarios[nombre_usuario] == password:
        messagebox.showinfo("Acceso Concedido", "¡Bienvenido!")
        ventana_login.destroy()
    else:
        messagebox.showerror("Error de Inicio de Sesión", "Credenciales incorrectas. Intente de nuevo.")





# Función para abrir la ventana del módulo de Usuarios
def abrir_modulo_usuarios():
    ventana_usuarios = tk.Toplevel(ventana_principal)
    ventana_usuarios.title("Módulo de Usuarios")

    # Etiquetas
    label_nombre = tk.Label(ventana_usuarios, text="Nombre de usuario:")
    label_password = tk.Label(ventana_usuarios, text="Contraseña:")

    # Campos de entrada
    entry_nombre = tk.Entry(ventana_usuarios)
    entry_password = tk.Entry(ventana_usuarios, show="*")

    # Botón para dar de alta usuario
    boton_alta_usuario = tk.Button(ventana_usuarios, text="Alta Usuario", command=lambda: alta_usuario(entry_nombre.get(), entry_password.get()))

    # Botón para dar de baja usuario
    boton_baja_usuario = tk.Button(ventana_usuarios, text="Baja Usuario", command=lambda: baja_usuario(entry_nombre.get()))

    # Botón para modificar usuario
    boton_modificar_usuario = tk.Button(ventana_usuarios, text="Modificar Usuario", command=lambda: modificar_usuario(entry_nombre.get(), entry_password.get()))

    label_nombre.pack()
    entry_nombre.pack()
    label_password.pack()
    entry_password.pack()
    boton_alta_usuario.pack()
    boton_baja_usuario.pack()
    boton_modificar_usuario.pack()

def alta_usuario(nombre, password):
    if nombre and password:
        usuarios[nombre] = password
        guardar_datos(usuarios, "Usuarios.txt")
        messagebox.showinfo("Alta de Usuario", f"Usuario '{nombre}' dado de alta con éxito.")
    else:
        messagebox.showerror("Error", "Debes ingresar un nombre de usuario y contraseña.")

def baja_usuario(nombre):
    if nombre in usuarios:
        del usuarios[nombre]
        guardar_datos(usuarios, "Usuarios.txt")
        messagebox.showinfo("Baja de Usuario", f"Usuario '{nombre}' dado de baja con éxito.")
    else:
        messagebox.showerror("Error", "Usuario no encontrado.")

def modificar_usuario(nombre, nueva_password):
    if nombre in usuarios:
        usuarios[nombre] = nueva_password
        guardar_datos(usuarios, "Usuarios.txt")
        messagebox.showinfo("Modificación de Usuario", f"Contraseña del usuario '{nombre}' modificada con éxito.")
    else:
        messagebox.showerror("Error", "Usuario no encontrado.")











# Función para abrir la ventana del módulo de Clientes
def abrir_modulo_clientes():
    ventana_clientes = tk.Toplevel(ventana_principal)
    ventana_clientes.title("Módulo de Clientes")

    # Etiquetas y campos de entrada para Alta Cliente
    label_codigo_cliente = tk.Label(ventana_clientes, text="Código del cliente:")
    label_codigo_cliente.pack()
    entry_codigo_cliente = tk.Entry(ventana_clientes)
    entry_codigo_cliente.pack()

    label_nombre_cliente = tk.Label(ventana_clientes, text="Nombre del cliente:")
    label_nombre_cliente.pack()
    entry_nombre_cliente = tk.Entry(ventana_clientes)
    entry_nombre_cliente.pack()

    label_direccion_cliente = tk.Label(ventana_clientes, text="Dirección del cliente:")
    label_direccion_cliente.pack()
    entry_direccion_cliente = tk.Entry(ventana_clientes)
    entry_direccion_cliente.pack()

    label_telefono_cliente = tk.Label(ventana_clientes, text="Teléfono del cliente:")
    label_telefono_cliente.pack()
    entry_telefono_cliente = tk.Entry(ventana_clientes)
    entry_telefono_cliente.pack()

    label_nit_cliente = tk.Label(ventana_clientes, text="NIT del cliente:")
    label_nit_cliente.pack()
    entry_nit_cliente = tk.Entry(ventana_clientes)
    entry_nit_cliente.pack()

    # Botón para dar de alta al cliente
    def alta_cliente():
        codigo = entry_codigo_cliente.get()
        nombre = entry_nombre_cliente.get()
        direccion = entry_direccion_cliente.get()
        telefono = entry_telefono_cliente.get()
        nit = entry_nit_cliente.get()

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

    boton_alta_cliente = tk.Button(ventana_clientes, text="Dar de Alta Cliente", command=alta_cliente)
    boton_alta_cliente.pack()

    # Etiqueta y campo de entrada para Baja Cliente
    label_codigo_baja_cliente = tk.Label(ventana_clientes, text="Código del cliente a dar de baja:")
    label_codigo_baja_cliente.pack()
    entry_codigo_baja_cliente = tk.Entry(ventana_clientes)
    entry_codigo_baja_cliente.pack()

    # Botón para dar de baja al cliente
    def baja_cliente():
        codigo = entry_codigo_baja_cliente.get()
        if codigo in clientes:
            del clientes[codigo]
            print("Cliente dado de baja con éxito.")
            guardar_datos(clientes, "Clientes.txt")
        else:
            print("Cliente no encontrado.")

    boton_baja_cliente = tk.Button(ventana_clientes, text="Dar de Baja Cliente", command=baja_cliente)
    boton_baja_cliente.pack()

    # Función para abrir la ventana de Modificación Cliente
    def abrir_modificacion_cliente():
        ventana_modificacion_cliente = tk.Toplevel(ventana_clientes)
        ventana_modificacion_cliente.title("Modificación Cliente")

        # Etiqueta y campo de entrada para el código del cliente a modificar
        label_codigo_modificacion_cliente = tk.Label(ventana_modificacion_cliente, text="Código del cliente a modificar:")
        label_codigo_modificacion_cliente.pack()
        entry_codigo_modificacion_cliente = tk.Entry(ventana_modificacion_cliente)
        entry_codigo_modificacion_cliente.pack()

        # Función para modificar al cliente
        def modificar_cliente():
            codigo = entry_codigo_modificacion_cliente.get()
            if codigo in clientes:
                cliente = clientes[codigo]
                print("\nRegistro de clientes")
                print(f"Codigo: {cliente['Codigo']}")
                print(f"Nombre: {cliente['Nombre']}")
                print(f"Direccion: {cliente['Direccion']}")
                print(f"Telefono: {cliente['Telefono']}")
                print(f"Nit: {cliente['Nit']}\n")

                nuevo_nombre = entry_nuevo_nombre.get()
                nuevo_direccion = entry_nueva_direccion.get()
                nuevo_telefono = entry_nuevo_telefono.get()
                nuevo_nit = entry_nuevo_nit.get()

                cliente["Nombre"] = nuevo_nombre
                cliente["Direccion"] = nuevo_direccion
                cliente["Telefono"] = nuevo_telefono
                cliente["Nit"] = nuevo_nit

                print("Cliente modificado con éxito.")
                guardar_datos(clientes, "Clientes.txt")
            else:
                print("Cliente no encontrado.")

        # Etiquetas y campos de entrada para la modificación del cliente
        label_nuevo_nombre = tk.Label(ventana_modificacion_cliente, text="Nuevo nombre del cliente:")
        label_nuevo_nombre.pack()
        entry_nuevo_nombre = tk.Entry(ventana_modificacion_cliente)
        entry_nuevo_nombre.pack()

        label_nueva_direccion = tk.Label(ventana_modificacion_cliente, text="Nueva dirección del cliente:")
        label_nueva_direccion.pack()
        entry_nueva_direccion = tk.Entry(ventana_modificacion_cliente)
        entry_nueva_direccion.pack()

        label_nuevo_telefono = tk.Label(ventana_modificacion_cliente, text="Nuevo teléfono del cliente:")
        label_nuevo_telefono.pack()
        entry_nuevo_telefono = tk.Entry(ventana_modificacion_cliente)
        entry_nuevo_telefono.pack()

        label_nuevo_nit = tk.Label(ventana_modificacion_cliente, text="Nuevo NIT del cliente:")
        label_nuevo_nit.pack()
        entry_nuevo_nit = tk.Entry(ventana_modificacion_cliente)
        entry_nuevo_nit.pack()

        # Botón para modificar al cliente
        boton_modificar_cliente = tk.Button(ventana_modificacion_cliente, text="Modificar Cliente", command=modificar_cliente)
        boton_modificar_cliente.pack()

    # Botón para abrir la ventana de Modificación Cliente
    boton_modificar_cliente = tk.Button(ventana_clientes, text="Modificar Cliente", command=abrir_modificacion_cliente)
    boton_modificar_cliente.pack()









# Función para abrir la ventana del módulo de Productos
def abrir_modulo_productos():
    ventana_productos = tk.Toplevel(ventana_principal)
    ventana_productos.title("Módulo de Productos")

    # Función para dar de alta un producto
    def alta_producto():
        codigo = entry_codigo.get()
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()

        if codigo and nombre and descripcion and precio and cantidad:
            producto = {
                "Codigo": codigo,
                "Nombre": nombre,
                "Descripcion": descripcion,
                "Precio": precio,
                "Cantidad": cantidad
            }

            productos[codigo] = producto
            guardar_datos(productos, "Productos.txt")
            messagebox.showinfo("Alta de Producto", f"Producto con código '{codigo}' dado de alta con éxito.")
        else:
            messagebox.showerror("Error", "Debes ingresar todos los campos del producto.")

    # Función para modificar la cantidad de inventario de un producto
    def modificacion_producto():
        codigo = entry_codigo_modificar.get()
        if codigo in productos:
            producto = productos[codigo]
            label_codigo.config(text=f"Codigo: {producto['Codigo']}")
            label_nombre.config(text=f"Nombre: {producto['Nombre']}")
            label_descripcion.config(text=f"Descripción: {producto['Descripcion']}")
            label_precio.config(text=f"Precio: {producto['Precio']}")
            label_cantidad.config(text=f"Cantidad: {producto['Cantidad']}")
            
            nueva_cantidad = entry_nueva_cantidad.get()
            if nueva_cantidad:
                producto["Cantidad"] = nueva_cantidad
                guardar_datos(productos, "Productos.txt")
                messagebox.showinfo("Modificación de Producto", f"Cantidad de producto con código '{codigo}' modificada con éxito.")
            else:
                messagebox.showerror("Error", "Debes ingresar la nueva cantidad en inventario.")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    # Función para consultar el inventario de un producto
    def consulta_inventario():
        codigo = entry_codigo_consultar.get()
        if codigo in productos:
            producto = productos[codigo]
            label_codigo_consultar.config(text=f"Codigo: {producto['Codigo']}")
            label_nombre.config(text=f"Nombre: {producto['Nombre']}")
            label_descripcion.config(text=f"Descripción: {producto['Descripcion']}")
            label_precio.config(text=f"Precio: {producto['Precio']}")
            label_cantidad.config(text=f"Cantidad: {producto['Cantidad']}")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    # Etiquetas y campos de entrada para alta de producto
    label_codigo = tk.Label(ventana_productos, text="Ingrese el código del producto:")
    entry_codigo = tk.Entry(ventana_productos)
    label_nombre = tk.Label(ventana_productos, text="Ingrese el nombre del producto:")
    entry_nombre = tk.Entry(ventana_productos)
    label_descripcion = tk.Label(ventana_productos, text="Ingrese la descripción del producto:")
    entry_descripcion = tk.Entry(ventana_productos)
    label_precio = tk.Label(ventana_productos, text="Ingrese el precio del producto:")
    entry_precio = tk.Entry(ventana_productos)
    label_cantidad = tk.Label(ventana_productos, text="Ingrese la cantidad en inventario del producto:")
    entry_cantidad = tk.Entry(ventana_productos)
    boton_alta = tk.Button(ventana_productos, text="Alta de Producto", command=alta_producto)

    # Etiqueta y campo de entrada para modificación de cantidad de inventario
    label_codigo_modificar = tk.Label(ventana_productos, text="Ingrese el código del producto a modificar:")
    entry_codigo_modificar = tk.Entry(ventana_productos)
    label_nueva_cantidad = tk.Label(ventana_productos, text="Ingrese la nueva cantidad en inventario del producto:")
    entry_nueva_cantidad = tk.Entry(ventana_productos)
    boton_modificacion = tk.Button(ventana_productos, text="Modificación de Producto", command=modificacion_producto)

    # Etiqueta y campo de entrada para consulta de inventario
    label_codigo_consultar = tk.Label(ventana_productos, text="Ingrese el código del producto a consultar:")
    entry_codigo_consultar = tk.Entry(ventana_productos)
    boton_consulta = tk.Button(ventana_productos, text="Consulta de inventario", command=consulta_inventario)

    label_codigo.pack()
    entry_codigo.pack()
    label_nombre.pack()
    entry_nombre.pack()
    label_descripcion.pack()
    entry_descripcion.pack()
    label_precio.pack()
    entry_precio.pack()
    label_cantidad.pack()
    entry_cantidad.pack()
    boton_alta.pack()
    label_codigo_modificar.pack()
    entry_codigo_modificar.pack()
    label_nueva_cantidad.pack()
    entry_nueva_cantidad.pack()
    boton_modificacion.pack()
    label_codigo_consultar.pack()
    entry_codigo_consultar.pack()
    boton_consulta.pack()
    label_codigo_consultar.pack()
    label_nombre.pack()
    label_descripcion.pack()
    label_precio.pack()
    label_cantidad.pack()




# Función para abrir la ventana del módulo de Categoría de Productos
def abrir_modulo_categorias():
    ventana_categorias = tk.Toplevel(ventana_principal)
    ventana_categorias.title("Módulo de Categoría de Productos")

    # Función para dar de alta una categoría
    def alta_categoria():
        codigo = entry_codigo.get()
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()

        if codigo and nombre and descripcion:
            categoria = {
                "Codigo": codigo,
                "Nombre": nombre,
                "Descripcion": descripcion
            }

            categorias[codigo] = categoria
            guardar_datos(categorias, "Categorias.txt")
            messagebox.showinfo("Alta de Categoría", f"Categoría con código '{codigo}' dada de alta con éxito.")
        else:
            messagebox.showerror("Error", "Debes ingresar todos los campos de la categoría.")

    # Función para dar de baja una categoría
    def baja_categoria():
        codigo = entry_codigo_baja.get()
        if codigo in categorias:
            del categorias[codigo]
            guardar_datos(categorias, "Categorias.txt")
            messagebox.showinfo("Baja de Categoría", f"Categoría con código '{codigo}' dada de baja con éxito.")
        else:
            messagebox.showerror("Error", "Categoría no encontrada.")

    # Función para generar el reporte de categorías
    def reporte_categorias():
        reporte = tk.Toplevel(ventana_categorias)
        reporte.title("Reporte de Categorías")
        
        for codigo, categoria in categorias.items():
            label_categoria = tk.Label(reporte, text="Registro de Categoría de producto")
            label_codigo = tk.Label(reporte, text=f"Código: {categoria['Codigo']}")
            label_nombre = tk.Label(reporte, text=f"Nombre: {categoria['Nombre']}")
            label_descripcion = tk.Label(reporte, text=f"Descripción: {categoria['Descripcion']}")

            label_categoria.pack()
            label_codigo.pack()
            label_nombre.pack()
            label_descripcion.pack()

    # Etiquetas y campos de entrada para alta de categoría
    label_codigo = tk.Label(ventana_categorias, text="Ingrese el código de la categoría:")
    entry_codigo = tk.Entry(ventana_categorias)
    label_nombre = tk.Label(ventana_categorias, text="Ingrese el nombre de la categoría:")
    entry_nombre = tk.Entry(ventana_categorias)
    label_descripcion = tk.Label(ventana_categorias, text="Ingrese la descripción de la categoría:")
    entry_descripcion = tk.Entry(ventana_categorias)
    boton_alta = tk.Button(ventana_categorias, text="Alta de Categoría", command=alta_categoria)

    # Etiquetas y campos de entrada para baja de categoría
    label_codigo_baja = tk.Label(ventana_categorias, text="Ingrese el código de la categoría a dar de baja:")
    entry_codigo_baja = tk.Entry(ventana_categorias)
    boton_baja = tk.Button(ventana_categorias, text="Baja de Categoría", command=baja_categoria)

    # Botón para generar el reporte de categorías
    boton_reporte = tk.Button(ventana_categorias, text="Reporte de Categorías", command=reporte_categorias)

    label_codigo.pack()
    entry_codigo.pack()
    label_nombre.pack()
    entry_nombre.pack()
    label_descripcion.pack()
    entry_descripcion.pack()
    boton_alta.pack()
    label_codigo_baja.pack()
    entry_codigo_baja.pack()
    boton_baja.pack()
    boton_reporte.pack()






# Función para abrir la ventana del módulo de Facturación
def abrir_modulo_facturacion():
    ventana_facturacion = tk.Toplevel(ventana_principal)
    ventana_facturacion.title("Módulo de Facturación")

    def facturar():
        # Lógica para la facturación, incluyendo la disminución de la cantidad de productos.
        pass

    def buscar_factura():
        numero_factura = entry_numero_factura.get()
        # Lógica para buscar y mostrar la factura.
        pass

    # Etiqueta para el encabezado de la factura
    label_encabezado_factura = tk.Label(ventana_facturacion, text="Supermercado 'EL ARABE'\n5 AVENIDA 8-9 El Triangulo zona 9\nTeléfono: 24201112")
    label_encabezado_factura.pack()

    # Etiqueta y campos de entrada para los datos de la factura
    label_nombre_cliente = tk.Label(ventana_facturacion, text="Nombre del cliente:")
    label_nombre_cliente.pack()
    entry_nombre_cliente = tk.Entry(ventana_facturacion)
    entry_nombre_cliente.pack()

    label_nit_cliente = tk.Label(ventana_facturacion, text="NIT del cliente:")
    label_nit_cliente.pack()
    entry_nit_cliente = tk.Entry(ventana_facturacion)
    entry_nit_cliente.pack()

    label_direccion_cliente = tk.Label(ventana_facturacion, text="Dirección del cliente:")
    label_direccion_cliente.pack()
    entry_direccion_cliente = tk.Entry(ventana_facturacion)
    entry_direccion_cliente.pack()

    label_fecha_factura = tk.Label(ventana_facturacion, text="Fecha (dd/mm/yyyy):")
    label_fecha_factura.pack()
    entry_fecha_factura = tk.Entry(ventana_facturacion)
    entry_fecha_factura.pack()

    # Etiqueta y campo de entrada para el código del producto
    label_codigo_producto = tk.Label(ventana_facturacion, text="Código del producto (0 para finalizar):")
    label_codigo_producto.pack()
    entry_codigo_producto = tk.Entry(ventana_facturacion)
    entry_codigo_producto.pack()

    # Botón para facturar
    boton_facturar = tk.Button(ventana_facturacion, text="Facturar", command=facturar)
    boton_facturar.pack()

    # Etiqueta para la sección de Buscar Factura
    label_buscar_factura = tk.Label(ventana_facturacion, text="Buscar Factura")
    label_buscar_factura.pack()

    # Etiqueta y campo de entrada para el número de factura a buscar
    label_numero_factura = tk.Label(ventana_facturacion, text="Ingrese el número de factura a buscar:")
    label_numero_factura.pack()
    entry_numero_factura = tk.Entry(ventana_facturacion)
    entry_numero_factura.pack()

    # Botón para buscar factura
    boton_buscar_factura = tk.Button(ventana_facturacion, text="Buscar Factura", command=buscar_factura)
    boton_buscar_factura.pack()

    # Área de visualización de la factura buscada
    text_factura = tk.Text(ventana_facturacion, height=10, width=50)
    text_factura.pack()








# Crear la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")

label_usuario = tk.Label(ventana_login, text="Usuario:")
label_password = tk.Label(ventana_login, text="Contraseña:")
entry_usuario = tk.Entry(ventana_login)
entry_password = tk.Entry(ventana_login, show="*")  # Mostrar asteriscos para ocultar la contraseña
boton_ingresar = tk.Button(ventana_login, text="Ingresar", command=validar_ingreso)

label_usuario.pack()
entry_usuario.pack()
label_password.pack()
entry_password.pack()
boton_ingresar.pack()

ventana_login.mainloop()

# Crear la ventana principal después del inicio de sesión
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Supermercado")

# Agregar botones para acceder a los módulos
boton_usuarios = tk.Button(ventana_principal, text="Usuarios", command=abrir_modulo_usuarios)
boton_clientes = tk.Button(ventana_principal, text="Clientes", command=abrir_modulo_clientes)
boton_productos = tk.Button(ventana_principal, text="Productos", command=abrir_modulo_productos)
boton_categorias = tk.Button(ventana_principal, text="Categoría de Productos", command=abrir_modulo_categorias)
boton_facturacion = tk.Button(ventana_principal, text="Facturación", command=abrir_modulo_facturacion)

boton_usuarios.pack()
boton_clientes.pack()
boton_productos.pack()
boton_categorias.pack()
boton_facturacion.pack()

ventana_principal.mainloop()
