import json
from datetime import datetime

ruta = 'ventapizza.json'
venta = []

precio_pizzas = {
    'Margarita': {'pequeña': 5500, 'Mediana': 8500, 'Familia': 11000},
    'Mexicana': {'pequeña': 7000, 'Mediana': 10000, 'Familia': 13000},
    'Barbacoa': {'pequeña': 6500, 'Mediana': 9500, 'Familia': 12500},
    'Vegetariana': {'pequeña': 5000, 'Mediana': 8000, 'Familia': 10500}
}

def registrar_venta():
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nombre_cliente = input("Nombre del cliente: ")
    tipo_cliente = input('Tipo de cliente (Estudiante diurno/Estudiante vespertino/Administrativo): ').capitalize()
    tipo_pizza = input('Tipo de pizza (Mexicana/Margarita/Barbacoa/Vegetariana): ').capitalize()
    tamaño_pizza = input("tamaño de la pizza (pequeña/mediana/Familia): ").capitalize()
    cantidad = int(input("Cantidad de pizzas: "))

    if tipo_pizza in precio_pizzas and tamaño_pizza in precio_pizzas[tipo_pizza]:
        precio_unitario = precio_pizzas[tipo_pizza][tamaño_pizza]
    else :
        print(f'Error: no se encontraron precio de pizza {tipo_pizza} de tamaño {tamaño_pizza}')
        return
    

    descuento = 0
    if tipo_cliente == 'estudiante diurno':
        descuento = 0.15
    elif tipo_cliente == 'estudiante vespertino':
        descuento = 0.18
    elif tipo_cliente == 'administrativo':
        descuento = 0.11

    precio_total = precio_unitario * cantidad
    precio_final = precio_total * (1 - descuento)

    ventas = {
        'fecha_hora': fecha_hora,
        'nombre_cliente': nombre_cliente,
        'tipo_cliente': tipo_cliente,
        'tipo_pizza': tipo_pizza,
        'tamaño_pizza': tamaño_pizza,
        'cantidad': cantidad,
        'precio_unitario': precio_unitario,
        'descuento': descuento,
        'precio_total': precio_total,
        'precio_final': precio_final
    }

    venta.append(ventas)
    print('Venta registrada con éxito!')

def mostrar_venta():
    if not venta :
        print('no hay venta registrada ')
    else :
        for ven in venta:
            print(ven)

def buscar_venta():
    nombre_cliente = input('Ingrese el nombre del cliente: ')
    ventas_cliente = [ven for ven in venta if ven["nombre_cliente"] == nombre_cliente]
    if not ventas_cliente:
        print(f'No se encontraron ventas para el cliente {nombre_cliente}.')
    else:
        for ven in ventas_cliente:
            print(ven)

def guardar_venta():
    with open(ruta, 'w') as file:
        json.dump(venta, file)
    print(f'Ventas guardadas en el archivo {ruta}.')

def cargar_venta():
    global venta
    try:
        with open(ruta, 'r') as file:
            venta = json.load(file)
        print(f'Ventas cargadas desde el archivo {ruta}.')
    except FileNotFoundError:
        print(f'No se encontró el archivo {ruta}.')

def generar_boleta():
    if not venta:
        print('No hay ventas registradas.')
    else:
        for ven in venta:
            print(ven)

def menu():
    while True:
        print("\n--- Sistema de Ventas de Pizzas ---")
        print("1. Registrar una venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar ventas por cliente")
        print("4. Guardar las ventas en un archivo")
        print("5. Cargar las ventas desde un archivo")
        print("6. Generar boleta de ventas")
        print("7. Salir")

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_venta()
        elif opcion == '3':
            buscar_venta()
        elif opcion == '4':
            guardar_venta()
        elif opcion == '5':
            cargar_venta()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción inválida. Por favor, ingrese una opción válida.')

menu()
