# 2626-POO-S9-Guachala-Milton

# Sistema de Restaurante

## Datos del estudiante

Nombre: Milton Paul Guachala Quinatoa

## Descripción del proyecto

El proyecto consiste en un sistema básico de administración de un restaurante desarrollado en Python.

El sistema permite registrar, buscar, actualizar, eliminar y listar productos, además de registrar y listar usuarios.

En esta semana se incorporaron las principales estructuras de datos de Python: listas, tuplas, diccionarios y conjuntos, utilizándolas para resolver necesidades concretas del sistema.

## Estructura del proyecto

Estructura esperada del repositorio:
Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── usuario.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md

## Responsabilidad de los componentes

producto.py: contiene la clase Producto con código, nombre, categoría y precio.
usuario.py: contiene la clase Usuario con identificación, nombre y correo.
restaurante.py: administra las listas de productos y usuarios y realiza las operaciones del sistema.
main.py: muestra el menú, solicita datos mediante consola y utiliza los métodos de Restaurante.
Estructuras de datos
List (list)

Se utiliza para almacenar las colecciones de productos y usuarios.

Tuple (tuple)

Se utiliza para almacenar las opciones del menú, ya que son datos que permanecen estables durante la ejecución.

Dict (dict)

Se utiliza para relacionar cada opción del menú con la función que debe ejecutarse.

Set (set)

Se utiliza para obtener las categorías de los productos sin elementos duplicados.

Ejecución

Abrir la terminal en la carpeta restaurante_app y ejecutar:

python main.py

Luego seleccionar las opciones del menú e ingresar los datos solicitados.

Reflexión

Elegir correctamente una estructura de datos permite organizar mejor la información y resolver cada necesidad del programa de forma adecuada. En este proyecto, cada estructura cumple una función diferente, haciendo que el sistema sea más organizado y fácil de administrar.