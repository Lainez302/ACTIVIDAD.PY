inventario = []

#AQUI SE AÑADIRA CUALQUIER PRODUCTO

def AGREGAR():
    print("\nINGRESE EL NUEVO PRODUCTO")
    nombre = input("INDIQUENOS EL NOMBRE:")
    while nombre == "":
        nombre = input("EL NOMBRE NO ES VALIDO:")

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    
    except ValueError:
        print("ERROR INDIQUE NUEVAMENTE LA CANTIDAD:")
        return

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("SE AGREGO CORRECTAMENTE EL PRODUCTO")

     #AQUI SE PUEDEN MIRAR LOS PRODUCTOS AGREGADOS

def buscar():
    print("\nQUE PRODUCTO QUIERES BUSCAR")
    nombre = input("INDICANOS QUE PRODUCTO ESTAS BUSCANDO:")
    for PRODUC in inventario:
        if PRODUC["nombre"] == nombre:
            print(f"Nombre: {PRODUC['nombre']}")
            print(f"Precio: ${PRODUC['precio']}")
            print(f"Cantidad: {PRODUC['cantidad']}")
            return
    print("ESTE PRODUCTO NO ESTA EN NUESTRO INVENTARIO")

#AQUI SE PUEDEN ACTUALIZAR LOS PRODUCTOS

def ACTUALIZAR():
    print("\nQUE VAMOS A ACTUALIZAR")
    nombre = input("SELECCIONA UN PRODUCTO A ACTUALIZAR")
    for PRODUC in inventario:
        if PRODUC["nombre"] == nombre:
            try:
                nuevo_precio = float(input("INGRESE EL NUEVO PRECIO:"))
                PRODUC["precio"] = nuevo_precio
                print("ACTUALIZASTE EL PRECIO DE UN PRODUCTO")
                return
            except ValueError:
                print("INGRESE UN PRECIO VALIDO")
                return
    print("ESTE PRODUCTO NO ESTA NE NUESTO INVENTARIO")


#AQUI SE PUEDE ELIMINAR UN PRODUCTO

def eliminar():
    print("\nELIMINAR UN PRODUCTO")
    nombre = input("QUE PRODUCTO DESEA ELIMINAR:")
    for iNVEN,PRODUC in enumerate(inventario):
        if PRODUC["nombre"]== nombre:
            inventario(iNVEN)
            print("SE ELIMINO EXITOSAMENTE")
            return
    print("ESTE PRODUCTO NO ESTA EN NUESTRO INVENTARIO")


#AQUI NUESTRO SISTEMA HACE UN CALCULO SOBRE EL INVENTARIO Y NOS MUESTRA LO QUE TENEMOS Y LOS PRECIOS

def calcular():
    print("\nCALCULAR EL INVENTARIO")
    if not inventario:
        print("AHORA MISMO NO EXISTEN PRODUCTOS")
        return
    total = sum(PRODUC["precio"] * PRODUC["cantidad"] for PRODUC in inventario)
    print(f"ESTE ES NUESTRO VALOR TOTAL ${total:.2f}")



def menu():
    print("\nINVENTARIO")
    print("1. AÑADIR UN NUEVO PRODUCTO ")
    print("2. BUSCAR UN PRODUCTO ")
    print("3. ACTUALIZAR UN PRODUCTO")
    print("4. ELIMINAR UN PRODUCTO")
    print("5. CALCULAR EL VALOR TOTAL")
   



def main():
    while True:
        menu()
        option = input("SELECCIONA UNA OPCION:")
        if option == "1":
            AGREGAR()
        elif option == "2":
            buscar()
        elif option == "3":
            ACTUALIZAR()
        elif option == "4":
            eliminar()
        elif option == "5":
            calcular()
        elif option == "6":
            break
        

if __name__ == "__main__":
    main()

    