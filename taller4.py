def mostrarMenu():
    print("=======MENÚ=======")
    print("1. agregar vehiculo")
    print("2. buscar vehiculo")
    print("3. eliminar vehiculo")
    print("4. actualizar disponibilidad")
    print("5. mostrar vehiculos")
    print("6. salir")
    print("===================")

def solicitarOpcion():
    try:
        opcion = input("ingrese una opcion: ")

        if opcion < 0 or opcion > 6:
            print("ingrese una opcion valida (1-6)")

        return opcion
    except ValueError:
        print("ingrese una opcion valida (1-6)")


def validarAnio(anioValidar):
    try:
        anioValidar = int(anioValidar)

        if anioValidar <= 1900:
            return False
        else:
            return True
        
    except ValueError:
        return False

def validarModelo(modeloValidar):
    if modeloValidar.strip() == "":
        return False
    else:
        return True
    
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
    
    modelo = input("ingrese el modelo del vehiculo: ")
    anio = input("ingrese el año del vehiculo: ")
    precio = input("ingrese el precio del vehiculo: ")

    modeloValido = validarModelo(modelo)
    anioValido = validarAnio(anio)
    precioValido = validarPrecio(precio)

    if modeloValido == True and anioValido == True and precioValido == True:    
        vehiculo = {
            "modelo": modelo,
            "anio": int(anio),
            "precio": float(precio),
            "disponible": False           
        }

        lista.append(vehiculo)
    else:
        print("los datos no cumpolen con las validaciones")

def buscarVahiculo(lista, modelo):
    
    for indice, vehiculo in enumerate(lista):
        if vehiculo["modelo"] == modelo:
            return indice
    
    return -1

def actualizarVehiculos(lista):

    for vehiculo in lista:
        if vehiculo['anio'] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

    print("se actualizaron los registros de vehiculos")

def mostrarVehiculos(lista):
    if len(lista) == 0:
        print("no existen vehiculos registrados aun")
        return

    actualizarVehiculos(lista)

    print("===Lista de vehiculos===")
    for vehiculos in lista:
        print(f"modelo: {vehiculos['modelo']}")
        print(f"precio: {vehiculos['precio']}")
        print(f"año: {vehiculos['anio']}")

        if vehiculos['disponible']:
            print(f"disponible?: DISPONIBLE")
        else:
            print(f"disponible?: NO DISPONIBLE")



########## Codigo principal ##########

ListaVehiculos = []

while True:
    
    mostrarMenu()

    opcionSeleccionada = solicitarOpcion()

    if opcionSeleccionada == 1:
        agregarVehiculo(ListaVehiculos)

    elif opcionSeleccionada == 2:

        modelobuscado = input("ingrese el modelo del vehiculo buscado: ")

        posicion = buscarVahiculo(ListaVehiculos, modelobuscado)

        if posicion != -1:
            print(f"vehiculo encontrado en la posicion {posicion}")

            vehiculoEncontrado = ListaVehiculos[posicion]

            print(f"modelo: {vehiculoEncontrado['modelo']}")
            print(f"precio: {vehiculoEncontrado['precio']}")
            print(f"año: {vehiculoEncontrado['anio']}")
            print(f"disponible?: {vehiculoEncontrado['disponible']}")
        else:
            print(f"el vehiculo '{modelobuscado}' no se encuentra registrado.")

    elif opcionSeleccionada == 3:
        
        modelobuscado = input("ingrese el modelo del vehiculo buscado: ")

        posicion = buscarVahiculo(ListaVehiculos, modelobuscado)

        if posicion != -1:
            ListaVehiculos.pop(posicion)

            print(f"vehiculo con modelo '{modelobuscado}' eliminado")
        else:
            print(f"el vehiculo '{modelobuscado}' no se encuentra registrado.")

    elif opcionSeleccionada == 4:
        actualizarVehiculos(ListaVehiculos)

    elif opcionSeleccionada == 5:
        mostrarVehiculos(ListaVehiculos)

    elif opcionSeleccionada == 6:
        print("gracias por usar nuestro sistema, vuelva pronto.")
        break





        