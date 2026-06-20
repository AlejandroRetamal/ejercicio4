
def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("=====================================")

def solicitarOpcion():
    while True:
        try:
            opcion = int(input("ingrese una opcion: "))

            if opcion < 0 or opcion > 6:
                print("ingrese una opcion valida (1-6)")
            else:
                return opcion
            
        except ValueError:
            print("ingrese una opcion valida (1-6)")

def validarModelo(modeloValidar):
    if modeloValidar.strip() == "":
        return False
    else:
        return True
    
def validarAnio(anioValidar):
    try:
        anioValidar = int(anioValidar)

        if anioValidar <= 1900:
            return False
        else:
            return True
    except ValueError:
        return False
    
def validarPrecio(precioValidar):
    try:
        precioValidar = float(precioValidar)

        if precioValidar <= 0:
            return False
        else:
            return True
    except ValueError:
        return False

def agregarVehiculo(lista):

    modelo = input("ingrese modelo del vehiculo: ")
    anio = input("ingrese el año del vehiculo: ")
    precio = input("ingrese el precio del vehiculo: ")

    modeloValidado = validarModelo(modelo)
    anioValidado = validarAnio(anio)
    precioValidado = validarPrecio(precio)

    if modeloValidado == True and anioValidado == True and precioValidado == True:
        vehiculo = {
            "modelo": modelo,
            "anio": int(anio),
            "precio": float(precio),
            "disponible": False
        }

        lista.append(vehiculo)

    else:
        print("los datos no cumplen con la validacion")


    
def buscarVehiculo(lista, modelo):

    for indice, vehiculo in enumerate(lista):
        if vehiculo['modelo'] == modelo:
            return indice
        
    return -1

def actualizarVehiculos(lista):

    for vehiculo in lista:
        if vehiculo['anio'] >= 2020:
            vehiculo['disponible'] = True
        else:
            vehiculo['disponible'] = False

    print("se actualizaron los registros de vehiculos")

def MostrarVehiculos(lista):

    if len(lista) == 0:
        print("no existen vehiculos registrados aun")
        return

    actualizarVehiculos(lista)

    print("=== LISTA DE VEHICULOS ===")
    for vehiculo in lista:
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"año: {vehiculo['anio']}")
        print(f"precio: {vehiculo['precio']}")

        if vehiculo['disponible']:
            print("Disponibilidad: DISPONIBLE")
        else:
            print("Disponibilidad: NO DISPONIBLE")


####### codigo principal#######

ListaVehiculos = []

while True:

    mostrarMenu()
    opcionSeleccionada = solicitarOpcion()

    if opcionSeleccionada == 1:
        agregarVehiculo(ListaVehiculos)

    elif opcionSeleccionada == 2:
        
        vehiculoBuscado = input("ingrese vehiculo a buscar: ")

        posicion = buscarVehiculo(ListaVehiculos, vehiculoBuscado)
    
        if posicion != -1:
            print(f"Vehiculo encontrado en la posicion {posicion}")
            vehiculoEncontrado = ListaVehiculos[posicion]

            print(f"modelo: {vehiculoEncontrado['modelo']}")
            print(f"año: {vehiculoEncontrado['anio']}")
            print(f"precio: {vehiculoEncontrado['precio']}")
            print(f"disponibilidad: {vehiculoEncontrado['disponible']}")
        else:
            print(f"El vehiculo {vehiculoBuscado} no se encuentra registrado")

    elif opcionSeleccionada == 3:
        vehiculoBuscado = input("ingrese vehiculo a buscar: ")

        posicion = buscarVehiculo(ListaVehiculos, vehiculoBuscado)              

        if posicion != -1:
            ListaVehiculos.pop(posicion)

            print(f"vehiculo {vehiculoBuscado} eliminado")
        else:
            print(f"El vehículo {vehiculoBuscado} no se encuentra registrado.")


    elif opcionSeleccionada == 4:
        actualizarVehiculos(ListaVehiculos)

    elif opcionSeleccionada == 5:
        MostrarVehiculos(ListaVehiculos)

    elif opcionSeleccionada == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
