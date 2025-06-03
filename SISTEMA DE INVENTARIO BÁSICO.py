import csv
import os

ARCHIVO_CSV = "inventario.csv"


def mostrar_menu():
    print("""
====== SISTEMA DE INVENTARIO - TIENDA DE PRODUCTOS ORGÁNICOS ======

1. Agregar producto
2. Buscar producto por ID
3. Mostrar inventario
4. Editar producto
5. Eliminar producto
6. Salir
""")


def cargar_inventario():
    inventario = []
    if not os.path.exists(ARCHIVO_CSV):
        return inventario

    with open(ARCHIVO_CSV, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            inventario.append({
                "id": int(fila["id"]),
                "nombre": fila["nombre"],
                "precio": float(fila["precio"]),
                "cantidad": int(fila["cantidad"])
            })
    return inventario


def guardar_inventario(inventario):
    with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["id", "nombre", "precio", "cantidad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for producto in inventario:
            escritor.writerow(producto)


def agregar_producto(inventario, siguiente_id):
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("⚠️ Datos inválidos. Intenta de nuevo.\n")
        return siguiente_id

    producto = {
        "id": siguiente_id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    guardar_inventario(inventario)
    print(f"✅ Producto '{nombre}' agregado con ID {siguiente_id}.\n")
    return siguiente_id + 1


def buscar_producto(inventario):
    try:
        id_buscar = int(input("🔎 Ingresa el ID del producto a buscar: "))
    except ValueError:
        print("⚠️ ID inválido. Intenta de nuevo.\n")
        return

    for producto in inventario:
        if producto["id"] == id_buscar:
            print("✅ Producto encontrado:")
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}\n")
            return

    print(f"❌ Producto con ID {id_buscar} no encontrado.\n")


def mostrar_inventario(inventario):
    if not inventario:
        print("📭 El inventario está vacío.\n")
        return

    print("\n====== INVENTARIO COMPLETO ======")
    for producto in inventario:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
    print()


def editar_producto(inventario):
    try:
        id_editar = int(input("✏️ Ingresa el ID del producto a editar: "))
    except ValueError:
        print("⚠️ ID inválido. Intenta de nuevo.\n")
        return

    for producto in inventario:
        if producto["id"] == id_editar:
            print(f"Producto actual: {producto}")
            nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            nuevo_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")

            if nuevo_nombre:
                producto["nombre"] = nuevo_nombre
            if nuevo_precio:
                try:
                    producto["precio"] = float(nuevo_precio)
                except ValueError:
                    print("⚠️ Precio inválido. Se mantiene el valor anterior.")
            if nuevo_cantidad:
                try:
                    producto["cantidad"] = int(nuevo_cantidad)
                except ValueError:
                    print("⚠️ Cantidad inválida. Se mantiene el valor anterior.")

            guardar_inventario(inventario)
            print("✅ Producto actualizado correctamente.\n")
            return

    print(f"❌ Producto con ID {id_editar} no encontrado.\n")


def eliminar_producto(inventario):
    try:
        id_eliminar = int(input("🗑️ Ingresa el ID del producto a eliminar: "))
    except ValueError:
        print("⚠️ ID inválido. Intenta de nuevo.\n")
        return

    for producto in inventario:
        if producto["id"] == id_eliminar:
            confirmacion = input(f"¿Seguro que quieres eliminar '{producto['nombre']}'? (si/no): ").lower()
            if confirmacion == "si":
                inventario.remove(producto)
                guardar_inventario(inventario)
                print("✅ Producto eliminado correctamente.\n")
            else:
                print("❎ Cancelado.\n")
            return

    print(f"❌ Producto con ID {id_eliminar} no encontrado.\n")


def main():
    inventario = cargar_inventario()
    siguiente_id = max([producto["id"] for producto in inventario], default=0) + 1

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            siguiente_id = agregar_producto(inventario, siguiente_id)
        elif opcion == "2":
            buscar_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            editar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()
