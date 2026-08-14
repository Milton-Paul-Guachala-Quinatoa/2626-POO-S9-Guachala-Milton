from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Mostrar categorias"),
    ("0", "Salir"),
)


def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar producto ---")

    codigo = pedir_texto("Codigo: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoria: ")

    try:
        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
        )

        registrado = restaurante.registrar_producto(producto)

        if registrado:
            print("Producto registrado correctamente.")
        else:
            print("El codigo ya se encuentra registrado.")

    except ValueError as error:
        print(error)


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar producto ---")

    codigo = pedir_texto("Codigo del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto)


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar producto ---")

    codigo = pedir_texto("Codigo del producto: ")

    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return

    nuevo_nombre = pedir_texto("Nuevo nombre: ")
    nueva_categoria = pedir_texto("Nueva categoria: ")

    try:
        nuevo_precio = float(input("Nuevo precio: "))

        actualizado = restaurante.actualizar_producto(
            codigo,
            nuevo_nombre,
            nueva_categoria,
            nuevo_precio,
        )

        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    except ValueError as error:
        print(error)


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar producto ---")

    codigo = pedir_texto("Codigo del producto: ")

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de productos ---")

    productos = restaurante.listar_productos()

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for indice, producto in enumerate(productos):
        print(f"{indice + 1}. {producto}")

    print(f"\nTotal de productos: {restaurante.contar_productos()}")


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")

    identificacion = pedir_texto("Identificacion: ")
    nombre = pedir_texto("Nombre: ")
    correo = pedir_texto("Correo: ")

    try:
        usuario = Usuario(
            identificacion,
            nombre,
            correo,
        )

        registrado = restaurante.registrar_usuario(usuario)

        if registrado:
            print("Usuario registrado correctamente.")
        else:
            print("La identificacion ya se encuentra registrada.")

    except ValueError as error:
        print(error)


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de usuarios ---")

    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for indice, usuario in enumerate(usuarios):
        print(f"{indice + 1}. {usuario}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorias unicas ---")

    categorias = restaurante.obtener_categorias_unicas()

    if len(categorias) == 0:
        print("No hay categorias registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def ejecutar_menu() -> None:
    restaurante = Restaurante()

    opciones = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        mostrar_menu()

        opcion = pedir_texto("Seleccione una opcion: ")

        if opcion == "0":
            print("Gracias por usar Sistema de Restaurante , que tengas un excelente día.")
            break

        accion = opciones.get(opcion)

        if accion is None:
            print("Opcion invalida.")
        else:
            accion(restaurante)


if __name__ == "__main__":
    ejecutar_menu()