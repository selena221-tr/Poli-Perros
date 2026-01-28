import random 
import os 
import sys 
from PIL import Image

# Diccionario para almacenar los datos
datosPoliperros = {
    "nombre": [],
    "huella dactilar": [],
    "foto": []
}

# Función para manejar rutas de recursos en .exe o en desarrollo
def resource_path(relative_path):
    """ Devuelve la ruta absoluta al recurso, funciona para dev y .exe """
    try:
        # PyInstaller crea una carpeta temporal llamada _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Menú principal
def menu():
    print("\n*** Bienvenido(a) ***\n")
    print("¿Qué acción desea realizar?")
    print("1) Registrar Poliperro")
    print("2) Mostrar Poliperros")
    print("3) Imprimir BBD")
    print("4) Mostrar un poliperro")
    print("5) Salir del sistema")
    opcion = input("Ingrese la opcion: ")
    return int(opcion) if opcion.isdigit() else 0

# Registrar poliperros
def registrarPoliperros(numPerros):
    os.makedirs("BDDPERROS", exist_ok=True)
    archivo = open("poliperros.txt", "a")

    for i in range(numPerros):
        print(f"\nIngrese los datos del poliperro {i+1}")
        nombre = input("Nombre: ")
        huellaDactilar = input("Huella Dactilar: ")

        tieneFoto = input("¿El poliperro tiene foto? (si/no): ").lower()
        if tieneFoto == "si":
            rutaOriginal = input("Ingrese la ruta de la foto: ")
            try:
                ima = Image.open(rutaOriginal)
            except:
                print("No se pudo abrir la imagen, usando foto por defecto.")
                ima = Image.open(resource_path("cargarPC/dog.png"))
        else:
            ima = Image.open(resource_path("cargarPC/dog.png"))

        rutaGuardada = f"BDDPERROS/poliperro_{random.randint(1,1000)}.png"
        ima.save(rutaGuardada)

        datosPoliperros["nombre"].append(nombre)
        datosPoliperros["huella dactilar"].append(huellaDactilar)
        datosPoliperros["foto"].append(rutaGuardada)

        archivo.write(f"{nombre} -- {huellaDactilar} -- {rutaGuardada}\n")

    archivo.close()
    print(f"\n{numPerros} poliperros registrados correctamente!")

# Mostrar todos los poliperros
def mostrarPoliperros():
    if len(datosPoliperros["nombre"]) == 0:
        print("No hay poliperros registrados.")
        return

    for i in range(len(datosPoliperros["nombre"])):
        print("-------------------------")
        print(f"Poliperro {i+1}:")
        print("* Nombre:", datosPoliperros["nombre"][i])
        print("* Huella Dactilar:", datosPoliperros["huella dactilar"][i])
        print("* Foto:", datosPoliperros["foto"][i])
        try:
            imagen = Image.open(datosPoliperros["foto"][i])
            imagen.show()
        except:
            print("No se pudo abrir la imagen.")

# Imprimir archivo de registros
def imprimirArchivo():
    if not os.path.exists("poliperros.txt"):
        print("No existe la BDD de poliperros.")
        return

    with open("poliperros.txt", "r") as archivo:
        lineas = archivo.readlines()
        for l in lineas:
            print(l, end=" ")

# Mostrar un poliperro por huella dactilar
def mostrarUnPoliperro():
    if len(datosPoliperros["nombre"]) == 0:
        print("No hay poliperros registrados.")
        return

    buscado = input("Ingrese la huella dactilar del poliperro: ")
    encontrado = False

    for i in range(len(datosPoliperros["huella dactilar"])):
        if datosPoliperros["huella dactilar"][i] == buscado:
            print("* Nombre:", datosPoliperros["nombre"][i])
            print("* Huella Dactilar:", datosPoliperros["huella dactilar"][i])
            print("* Foto:", datosPoliperros["foto"][i])
            try:
                imagen = Image.open(datosPoliperros["foto"][i])
                imagen.show()
            except:
                print("No se pudo abrir la imagen.")
            encontrado = True
            break

    if not encontrado:
        print("Poliperro no encontrado.\n")

# Función principal
def main():
    print("---------------- POLIPERROS --------------")
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            numPerros = input("Ingrese el numero de poliperros a registrar: ")
            if numPerros.isdigit():
                registrarPoliperros(int(numPerros))
            else:
                print("Debe ingresar un número válido.")
        elif opcion == 2:
            mostrarPoliperros()
        elif opcion == 3:
            imprimirArchivo()
        elif opcion == 4:
            mostrarUnPoliperro()
        else:
            print("Opción inválida.")
        opcion = menu()

    print("Gracias por usar el sistema")

if __name__ == "__main__":
    main()







    
  
  

  









