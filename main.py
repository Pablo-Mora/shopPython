nameSheller = "Pablo Mora"

invoide_number = 1

invoices = []

products = []
product = {}

clients = []
client = {}

ban = 0

def switch( ban ):
    global invoide_number
    global products

    if ban == 1:
        print("NUEVO PRODUCTO")
        print("\n \n \n")
        print("Ingrese el codigo:", end="")
        codeProduct = input()
        print("Ingrese el nombre:", end="")
        nameProduct = input()
        print("Ingrese la cantidad:", end="")
        cant = input()
        print("Ingrese el valor:", end="")
        valueProduct = input()

        product = {
            'code': codeProduct,
            'name': nameProduct,
            'cant': cant,
            'value': valueProduct
        }

        products.append(product)

        print(f"Producto {nameProduct} agregado correctamente.")

    elif ban == 2:
        print("ELIMINAR PRODUCTO")
        print("\n \n \n")
        print("Digite el codigo:", end="")
        codeProduct = input()
        deleteConfirmation = 0
        while deleteConfirmation != 1:
            print("¿Desea eliminar el producto? (yes= 1/ no = 0)")
            deleteConfirmation = int(input())

        products = [p for p in products if p['code'] != codeProduct]
        print("Producto eliminado correctamente.")

    elif ban == 3:
        print("LISTA DE PRODUCTOS")
        print("\n \n \n")
        if len(products) == 0:
            print("No hay productos registrados.")
        else:
            for product in products:
                print(f"Codigo: {product['code']} - \nNombre {product['name']} - \nCantidad {product['cant']} - \nPrecio {product['value']}")
    elif ban == 4:
        print("REALIZAR FACTURA")
        print("\n \n \n")
        idClient = None
        nameClient = None
        print("Cedula: ", end="")
        idClient = input()
        print("Nombre del cliente: ", end="")
        nameClient = input()

        client = {
            'Cedula': idClient,
            'Nombre': nameClient
        }

        clients.append(client)

        global invoide_number
        new_invoice = {
            'invoide_id':invoide_number,
            'products': products,
            'total': sum(float(product['value']) for product in products)
        }

        invoices.append(new_invoice)

        print(f"Nuevo cliente \nFactura {invoide_number:04d} - \nCedula {client['Cedula']} - \nNombre {client['Nombre']} \nFactura 001  \ntotal de la factura")
        invoide_number += 1
        print("... Imprimiendo Factura ...")
    elif ban == 5:
        print("CANCELAR LA FACTURA")
        print("\n \n \n")

        print("Ingrese el número de la factura a cancelar:")
        cancel_invoice_id = int(input())

        invoice_found = False
        for invoice in invoices:
            if invoice['invoide_id'] == cancel_invoice_id:
                invoices.remove(invoice)
                print(f"Factura {cancel_invoice_id:04d} cancelada corectamente.")
                invoice_found = True
                break
            elif invoice_found:
                print(f"Factura {cancel_invoice_id:04d} no encontrada.")
   
    elif ban == 6:
        print("!!Hasta luego, vuelva pronto!!")
        return False
    else:
        print("Opcion no valida vuelva a intentar")
        return True
    return True
        
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