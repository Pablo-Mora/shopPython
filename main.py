nameSheller = "Pablo Mora"

products = []
product = {}

ban = 0

def switch( ban ):
    if ban == 1:
        print("NUEVO PRODUCTO")
        print("Ingrese el codigo:", end="")
        codeProduct = input()
        print("Ingrese el nombre:", end="")
        nameProduct = input()
        print("Ingrese el valor:", end="")
        valueProduct = input()
    elif ban == 2:
        print("ELIMINAR PRODUCTO")
        print("Digite el codigo:", end="")
        codeProduct = input()
        deleteConfirmation = 0
        while deleteConfirmation != 1:
            print("¿Desea eliminar el producto? (yes= 1/ no = 0)")
            deleteConfirmation = int(input())

            print("Producto eliminado correctamente")
    elif ban == 3:
        print("LISTA DE PRODUCTOS")
    elif ban == 4:
        print("REALIZAR FACTURA")
        print("Nuevo cliente  \nFactura 001  \ntotal de la factura")
    elif ban == 5:
        print("CANCELAR LA FACTURA")
        cancelInvoide = 0
        while deleteConfirmation != 1:
            print("¿Desea cancelar la factura? (yes= 1/ no = 0)")
            cancelInvoide = int(input())

            print("Factura cancelada corectamente")
    elif ban == 6:
        print("!!Hasta luego, vuelva pronto!!")
    else:
        return None
        
while switch( ban ) != 6:
    print("!Bienvenido sr@," + nameSheller + "!")
    print("------ Menú de Opciones ------")
    print("1. Nuevo producto")
    print("2. Eliminar producto")
    print("3. Lista de productos")
    print("4. Realizar factura")
    print("5. Cancelar factura")
    print("6. salir")

    print("Digite la opción que desea:")
    ban = int(input())