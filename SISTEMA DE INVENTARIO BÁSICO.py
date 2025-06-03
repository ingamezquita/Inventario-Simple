print('*** TIENDA DE ROPA  ***')

inventario = []

cantidad_productos = int(input('¿Cuántos productos ingresas al inventario? '))

for indice in range(cantidad_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    # Diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario
print(f'\nInventario: {inventario}')

# Buscar un producto por id

inventario = [
    {'id': 1, 'nombre': 'Producto A', 'precio': 10.0, 'cantidad': 5},
    {'id': 2, 'nombre': 'Producto B', 'precio': 20.0, 'cantidad': 3},
    # Agrega más productos según sea necesario
]

while True:
    try:
        id_buscar = int(input('\nIngresa el serial de registro (ID) del producto a buscar: '))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    producto_encontrado = None

    for producto in inventario:
        if producto.get('id') == id_buscar:
            producto_encontrado = producto
            break

    if producto_encontrado is not None:
        print('Información del producto encontrado:')
        print(f'''Id: {producto_encontrado.get('id')}
Nombre: {producto_encontrado.get('nombre')}
Precio: {producto_encontrado.get('precio')}
Cantidad: {producto_encontrado.get('cantidad')}''')
    else:
        print(f'\nProducto con id {id_buscar} NO encontrado.')
        while True:
            busqueda_inventario = input('¿Deseas mirar el inventario completo? (si/no): ').lower()
            if busqueda_inventario in ['si', 'no']:
                break
            print('Por favor verifica que la palabra esté bien escrita (si/no).')

        if busqueda_inventario == 'si':
            print('\n--- Inventario Detallado ---')
            for producto in inventario:
                print(f'''Id: {producto.get('id')}
Nombre: {producto.get('nombre')}
Precio: ${producto.get('precio'):.2f}
Cantidad: {producto.get('cantidad')}''')
        else:
            print('Por favor, verifica nuevamente los datos del ID, gracias.')

    nueva_consulta = input('\n¿Deseas realizar otra consulta? (si/no): ').lower()
    if nueva_consulta != 'si':
        print('SALISTE DEL ÁREA DE BÚSQUEDA, GRACIAS.')
        break