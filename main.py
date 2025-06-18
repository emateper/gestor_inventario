"""
Interfaz de Usuario: Menú Principal
Para interactuar con su sistema de gestión de productos, deberán implementar
un menú principal que permita al usuario realizar las operaciones CRUD y de
persistencia de datos. Este menú se ejecutará en un bucle continuo hasta que el
usuario decida salir.
Detalles de Implementación del Menú:

1. Función Principal (main.py):
○ Dentro de la función principal de su script (típicamente llamada
main() o ejecutada directamente cuando el archivo se corre),
inicialicen una instancia de su clase Inventario.
○ Al inicio del programa, intenten cargar los productos desde el
archivo JSON predefinido (ej. "productos.json"). Manejen la
excepción FileNotFoundError si el archivo no existe aún, informando
al usuario que se iniciará con un inventario vacío.

2. Bucle del Menú:
○ Utilicen un bucle while True para mantener el menú en ejecución.
○ Dentro del bucle, muestren las opciones disponibles al usuario
de forma clara.
Opciones del Menú:
--- Menú de Gestión de Productos ---
1. Agregar nuevo producto
2. Listar todos los productos
3. Buscar producto por ID
4. Actualizar producto
5. Eliminar producto
6. Guardar productos (JSON)
7. Cargar productos (JSON)
8. Salir
------------------------------------
Ingrese su opción:

3. Captura de Entrada y Lógica:
○ Utilicen input() para capturar la opción del usuario.
○ Empleen una estructura if/elif/else o un match/case (Python 3.10+)
para ejecutar la lógica correspondiente a la opción elegida.

4. Detalle de cada Opción:
○ 1. Agregar nuevo producto:
■ Soliciten al usuario el tipo de producto a agregar (ej.
"electrónica" o "alimento").
■ Luego, pidan los datos específicos de cada producto (nombre,
precio, stock, y las propiedades adicionales de las clases
derivadas).
■ Manejen la creación de la instancia correcta
(ProductoElectronico o ProductoAlimento) y llamen al método
agregar_producto() de su Inventario.
■ Asegúrense de que el id sea generado automáticamente
(pueden usar un contador simple en la clase Inventario o uuid
para mayor robustez) y sea único.

○ 2. Listar todos los productos:
■ Simplemente llamen al método listar_productos() de su
Inventario. Si no hay productos, informen al usuario.

○ 3. Buscar producto por ID:
■ Soliciten el id del producto.
■ Llamen a buscar_producto_por_id(). Si el producto existe,
muestren sus detalles; de lo contrario, informen que el
producto no fue encontrado.

○ 4. Actualizar producto:
■ Soliciten el id del producto a actualizar.
■ Si el producto existe, pregunten qué propiedades desea
actualizar (nombre, precio, stock, etc.). Permitan actualizar
una o varias propiedades.
■ Construyan un diccionario con los nuevos_datos y llamen a
actualizar_producto().
■ Informen al usuario si la actualización fue exitosa o si el
producto no se encontró.

○ 5. Eliminar producto:
■ Soliciten el id del producto a eliminar.
■ Llamen a eliminar_producto(). Confirmen la eliminación o
informen si el producto no se encontró.

○ 6. Guardar productos (JSON):
■ Llamen al método guardar_productos_json(). Informen al
usuario que los datos han sido guardados exitosamente.

○ 7. Cargar productos (JSON):
■ Llamen al método cargar_productos_json(). Informen si la
carga fue exitosa o si el archivo no existe.
■ ¡Importante! Al cargar, deben re-instanciar los objetos de las
clases correctas (ProductoElectronico, ProductoAlimento,
etc.) basándose en alguna información guardada en el JSON
(por ejemplo, un campo tipo_producto).

○ 8. Salir:
■ Antes de salir, pregunten al usuario si desea guardar los
cambios actuales en el archivo JSON. Si la respuesta es
afirmativa, llamen a guardar_productos_json().
■ Utilicen break para salir del bucle while.

5. Manejo de Errores en la Entrada:
○ Utilicen bloques try-except para manejar posibles errores en la
entrada del usuario, como cuando se espera un número (ID, precio,
stock) y se ingresa texto.
○ Muestren mensajes de error claros al usuario para guiarlo.
Recuerden que disponen al menos de una clase de consulta, y estoy a la espera
del Excel con dudas que necesiten despejar.
Éxitos!!

"""


import json
import os

class Productos:     #creación de la clase base Productos
    def __init__(self, tipo, nombre, precio, stock, id=None):
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.id = id

    def to_dict(self):     #convierte la instancia en un diccionario mejor para serializar a JSON
        return {
            "tipo": self.tipo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "id": self.id
        }

    @classmethod
    def from_dict(cls, data): #convierte un diccionario en una instancia de la clase
        return cls(
            tipo=data["tipo"],
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            id=data["id"]
        )

class Discos(Productos):
    def __init__(self, nombre, precio, stock, id=None, artista=None, genero=None):
        super().__init__("disco", nombre, precio, stock, id)
        self.artista = artista
        self.genero = genero

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "artista": self.artista,
            "genero": self.genero
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            id=data["id"],
            artista=data["artista"],
            genero=data["genero"]
        )

class Libro(Productos):
    def __init__(self, nombre, precio, stock, id=None, autor=None, genero=None):
        super().__init__("libro", nombre, precio, stock, id)
        self.autor = autor
        self.genero = genero

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "autor": self.autor,
            "genero": self.genero
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            id=data["id"],
            autor=data["autor"],
            genero=data["genero"]
        )

class Revistas(Productos):
    def __init__(self, nombre, precio, stock, id=None, tema=None, periodicidad=None):
        super().__init__("revista", nombre, precio, stock, id)
        self.tema = tema
        self.periodicidad = periodicidad

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tema": self.tema,
            "periodicidad": self.periodicidad
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            id=data["id"],
            tema=data["tema"],
            periodicidad=data["periodicidad"]
        )

class Inventario:       #METODOS DE CRUD
    def __init__(self):
        self.productos = []
        self.file_path = "productos.json"
        self.cargar_productos_json()

    def crear(self, producto):    #1 Agregar un nuevo producto

        # Validaciones generales
        if not isinstance(producto, (Discos, Libro, Revistas)):
            raise TypeError("El producto debe ser una instancia de Discos, Libro o Revistas.")
        if not producto.nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not producto.tipo or producto.tipo not in ["disco", "libro", "revista"]:
            raise ValueError("El tipo de producto debe ser 'disco', 'libro' o 'revista'.")
        if producto.stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        if producto.precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        # Validaciones específicas por tipo
        if producto.tipo == "disco":
            if not isinstance(producto, Discos):
                raise TypeError("El producto debe ser una instancia de Discos.")
            if not getattr(producto, "artista", None) or not getattr(producto, "genero", None):
                raise ValueError("El disco debe tener un artista y un género.")
        elif producto.tipo == "libro":
            if not isinstance(producto, Libro):
                raise TypeError("El producto debe ser una instancia de Libro.")
            if not getattr(producto, "autor", None) or not getattr(producto, "genero", None):
                raise ValueError("El libro debe tener un autor y un género.")
        elif producto.tipo == "revista":
            if not isinstance(producto, Revistas):
                raise TypeError("El producto debe ser una instancia de Revistas.")
            if not getattr(producto, "tema", None) or not getattr(producto, "periodicidad", None):
                raise ValueError("La revista debe tener un tema y una periodicidad.")

        # Validaciones de unicidad
        for p in self.productos:
            if p.id == producto.id:
                raise ValueError(f"Ya existe un producto con el ID {producto.id}.")
            if p.tipo == producto.tipo and p.nombre == producto.nombre:
                raise ValueError(f"Ya existe un producto del tipo {producto.tipo} con el nombre {producto.nombre}.")

        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado correctamente.")
        self.guardar_productos_json()  # Guardar automáticamente después de agregar
        return producto

    def listar(self):           #2 Listar los productos
        if not self.productos:
            print("No hay productos en el inventario.")
            return []
        print("Lista de productos:")
        for producto in self.productos:
            print(f"ID: {producto.id}, Tipo: {producto.tipo}, Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")
            if isinstance(producto, Discos):
                print(f"  Artista: {producto.artista}, Género: {producto.genero}")
            elif isinstance(producto, Libro):
                print(f"  Autor: {producto.autor}, Género: {producto.genero}")
            elif isinstance(producto, Revistas):
                print(f"  Tema: {producto.tema}, Periodicidad: {producto.periodicidad}")
        print("Productos listados correctamente.")
        return self.productos

    def buscar_por_id(self, id_producto): #3 Buscar producto por ID
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    def actualizar(self, id_producto, nuevos_datos): #4 Actualizar producto
        if not isinstance(nuevos_datos, dict):
            raise TypeError("Los nuevos datos deben ser un diccionario.")
        if not nuevos_datos:
            raise ValueError("Los nuevos datos no pueden estar vacíos.")
        if "id" in nuevos_datos and nuevos_datos["id"] != id_producto:
            raise ValueError("No se puede cambiar el ID del producto.")
        if "tipo" in nuevos_datos and nuevos_datos["tipo"] not in ["disco", "libro", "revista"]:
            raise ValueError("El tipo de producto debe ser 'disco', 'libro' o 'revista'.")
        if "stock" in nuevos_datos and nuevos_datos["stock"] < 0:
            raise ValueError("El stock no puede ser negativo.")
        if "precio" in nuevos_datos and nuevos_datos["precio"] < 0:
            raise ValueError("El precio no puede ser negativo.")
        if "nombre" in nuevos_datos and not nuevos_datos["nombre"]:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if "tipo" in nuevos_datos:
            if nuevos_datos["tipo"] == "disco":
                if not isinstance(nuevos_datos, Discos):
                    raise TypeError("El producto debe ser una instancia de Discos.")
                if not nuevos_datos.get("artista") or not nuevos_datos.get("genero"):
                    raise ValueError("El disco debe tener un artista y un género.")
            elif nuevos_datos["tipo"] == "libro":
                if not isinstance(nuevos_datos, Libro):
                    raise TypeError("El producto debe ser una instancia de Libro.")
                if not nuevos_datos.get("autor") or not nuevos_datos.get("genero"):
                    raise ValueError("El libro debe tener un autor y un género.")
            elif nuevos_datos["tipo"] == "revista":
                if not isinstance(nuevos_datos, Revistas):
                    raise TypeError("El producto debe ser una instancia de Revistas.")
                if not nuevos_datos.get("tema") or not nuevos_datos.get("periodicidad"):
                    raise ValueError("La revista debe tener un tema y una periodicidad.")
        if "id" in nuevos_datos:
            for producto in self.productos:
                if producto.id == nuevos_datos["id"] and producto.id != id_producto:
                    raise ValueError(f"Ya existe un producto con el ID {nuevos_datos['id']}.")
        if "tipo" in nuevos_datos:
            for producto in self.productos:
                if (producto.tipo == nuevos_datos["tipo"] and
                    producto.nombre == nuevos_datos.get("nombre", producto.nombre) and
                    producto.id != id_producto):
                    raise ValueError(f"Ya existe un producto del tipo {nuevos_datos['tipo']} con el nombre {nuevos_datos.get('nombre', producto.nombre)}.")
        # Actualizar el producto
        if not id_producto:
            raise ValueError("El ID del producto a actualizar no puede ser None.")
        producto = self.buscar_por_id(id_producto)
        if producto:    # Si el producto existe, actualizamos sus atributos
            for key, value in nuevos_datos.items():
                setattr(producto, key, value)
                print(f"Producto {producto.nombre} actualizado correctamente.")
            self.guardar_productos_json()  # Guardar automáticamente después de actualizar
            return True
        return False

    def eliminar(self, id_producto):  #5 Eliminar producto
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print(f"Producto {producto.nombre} eliminado correctamente.")
            self.guardar_productos_json()  # Guardar automáticamente después de eliminar
            return True
        return False

    def guardar_productos_json(self): #6 Guardar productos en JSON
        if not self.productos:
            print("No hay productos para guardar.")
            return
        if not os.path.exists(os.path.dirname(self.file_path)) and os.path.dirname(self.file_path):
            os.makedirs(os.path.dirname(self.file_path))
        if not self.file_path.endswith('.json'):
            raise ValueError("La ruta del archivo debe terminar con '.json'.")
        with open(self.file_path, 'w') as file:
            json.dump([producto.to_dict() for producto in self.productos], file, indent=4)

    def cargar_productos_json(self):  #7 Cargar productos desde JSON
        if not os.path.exists(self.file_path):
            print(f"El archivo {self.file_path} no existe. Iniciando con un inventario vacío.")
            return
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    if item['tipo'] == 'disco':
                        producto = Discos.from_dict(item)
                    elif item['tipo'] == 'libro':
                        producto = Libro.from_dict(item)
                    elif item['tipo'] == 'revista':
                        producto = Revistas.from_dict(item)
                    else:
                        continue
                    self.crear(producto)
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {self.file_path}. Asegúrese de que el formato sea correcto.")
        except FileNotFoundError:
            print(f"El archivo {self.file_path} no existe. Iniciando con un inventario vacío.")
        except Exception as e:
            print(f"Error al cargar productos desde {self.file_path}: {e}")
            


def menu():
    print("\nBienvenido al sistema de gestión de productos")
    print("1. Agregar nuevo producto")
    print("2. Listar todos los productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Guardar productos (JSON)")
    print("7. Cargar productos (JSON)")
    print("8. Salir")
    return input("Seleccione una opción: ")


# Ejecución del menú
if __name__ == "__main__":
    productos = Inventario()  # Crear una instancia de Inventario
    biblioteca = productos  # Asignar la instancia a una variable para usar en el menú
    biblioteca.cargar_productos_json()  # Cargar productos al iniciar
    # Bucle del menú

    while True:
        opcion = menu()

        if opcion == "1":
            tipo_producto = input("Ingrese el tipo de producto (disco, libro, revista): ").strip().lower()
            nombre = input("Ingrese el nombre del producto: ").strip()
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            id_producto = len(biblioteca.productos) + 1
            if tipo_producto == "disco":
                artista = input("Ingrese el artista del disco: ").strip()
                genero = input("Ingrese el género del disco: ").strip()
                producto = Discos(nombre, precio, stock, id_producto, artista, genero)
            elif tipo_producto == "libro":
                autor = input("Ingrese el autor del libro: ").strip()
                genero = input("Ingrese el género del libro: ").strip()
                producto = Libro(nombre, precio, stock, id_producto, autor, genero)
            elif tipo_producto == "revista":
                tema = input("Ingrese el tema de la revista: ").strip()
                periodicidad = input("Ingrese la periodicidad de la revista: ").strip()
                producto = Revistas(nombre, precio, stock, id_producto, tema, periodicidad)
            else:
                print("Tipo de producto no válido.")
                continue
            try:
                biblioteca.crear(producto)
            except (TypeError, ValueError) as e:
                print(f"Error al agregar el producto: {e}")
        elif opcion == "2":
            biblioteca.listar()
        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto a buscar: "))
            producto = biblioteca.buscar_por_id(id_producto)
            if producto:
                print(f"Producto encontrado: {producto.to_dict()}")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nuevos_datos = {}
            nombre = input("Ingrese el nuevo nombre del producto (deje en blanco para no cambiar): ").strip()
            if nombre:
                nuevos_datos["nombre"] = nombre
            precio = input("Ingrese el nuevo precio del producto (deje en blanco para no cambiar): ")
            if precio:
                nuevos_datos["precio"] = float(precio)
            stock = input("Ingrese el nuevo stock del producto (deje en blanco para no cambiar): ")
            if stock:
                nuevos_datos["stock"] = int(stock)
            tipo_producto = input("Ingrese el nuevo tipo de producto (deje en blanco para no cambiar): ").strip().lower()
            if tipo_producto:
                nuevos_datos["tipo"] = tipo_producto
                if tipo_producto == "disco":
                    artista = input("Ingrese el nuevo artista del disco: ").strip()
                    genero = input("Ingrese el nuevo género del disco: ").strip()
                    nuevos_datos["artista"] = artista
                    nuevos_datos["genero"] = genero
                elif tipo_producto == "libro":
                    autor = input("Ingrese el nuevo autor del libro: ").strip()
                    genero = input("Ingrese el nuevo género del libro: ").strip()
                    nuevos_datos["autor"] = autor
                    nuevos_datos["genero"] = genero
                elif tipo_producto == "revista":
                    tema = input("Ingrese el nuevo tema de la revista: ").strip()
                    periodicidad = input("Ingrese la nueva periodicidad de la revista: ").strip()
                    nuevos_datos["tema"] = tema
                    nuevos_datos["periodicidad"] = periodicidad
            try:
                biblioteca.actualizar(id_producto, nuevos_datos)
            except (TypeError, ValueError) as e:
                print(f"Error al actualizar el producto: {e}")
        elif opcion == "5":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            if biblioteca.eliminar(id_producto):
                print("Producto eliminado correctamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == "6":
            try:
                biblioteca.guardar_productos_json()
                print("Productos guardados correctamente en JSON.")
            except Exception as e:
                print(f"Error al guardar productos: {e}")
        elif opcion == "7":
            try:
                biblioteca.cargar_productos_json()
                print("Productos cargados correctamente desde JSON.")
            except Exception as e:
                print(f"Error al cargar productos: {e}")
        elif opcion == "8":
            guardar_cambios = input("¿Desea guardar los cambios antes de salir? (s/n): ").strip().lower()
            if guardar_cambios == "s":
                try:
                    biblioteca.guardar_productos_json()
                    print("Cambios guardados correctamente.")
                except Exception as e:
                    print(f"Error al guardar cambios: {e}")
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print("\n")

