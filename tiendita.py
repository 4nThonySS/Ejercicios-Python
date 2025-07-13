PRODUCTOS = {
    1:{"nombre":"Pan", "precio":1000},
    2:{"nombre":"Leche", "precio":1200},
    3:{"nombre":"Queso", "precio":2500},
}
total_general = 0
total_cliente = 0
carrito = []
programa = True
while programa:

    while True:
        print("--- Menú -TienditaTienditaMia- ---")
        for i in PRODUCTOS:
            print(f"[{i}]. {PRODUCTOS[i]["nombre"]} - ${PRODUCTOS[i]["precio"]:,}")
        print("--------------------")
        print("[9]. Ver carrito")
        print("[0]. Finalizar")
        try:
            opc_menu = int(input("Selecciona una opción: "))
        except ValueError:
            print("ERROR: Formato invalido.")
            input("Presione ENTER para continuar...")
            continue
        if opc_menu == 0:
            programa = False
            break
        elif opc_menu == 9:
            print("")
            for producto in carrito:
                print(f"Producto: {producto['nombre']} - Precio: {producto['precio']:,} - Cantidad: {producto['cantidad']} - Subtotal: {producto['subtotal']:,}")
                total_cliente += producto['subtotal']
                print(f"Total a pagar: {total_cliente:,}\n")
                total_general += total_cliente
            if total_general == 0:
                print("No hubo pedidos")
                input("Presiona ENTER para continuar...")
            else:
                print(f"Total recaudado por la tiendita: ${total_general:,}")
                input("Presiona ENTER para continuar...")
        elif opc_menu not in PRODUCTOS:
            print("ERROR: Opción invalida.")
            input("Presione ENTER para continuar...")
            continue
        else:
            while True:
                cantidad = int(input("Selecciona una cantidad: "))
                if cantidad <= 0:
                    print("ERROR: La cantidad no puede ser menor o igual a 0.")
                    input("Presione ENTER para continuar...")
                    continue
                else:
                    
                    producto = PRODUCTOS[opc_menu]["nombre"]
                    precio = PRODUCTOS[opc_menu]["precio"]
                    subtotal = precio * cantidad
                    print(f"Agregado: {producto}: {precio} X {cantidad} = ${subtotal:,}")
                    carrito.append({
                    "nombre": producto,
                    "precio": precio,
                    "cantidad": cantidad,
                    "subtotal": subtotal
                })
                    break

print("---Resumen Tiendita---")
for producto in carrito:
    print(f"Producto: {producto['nombre']} - Precio: {producto['precio']:,} - Cantidad: {producto['cantidad']} - Subtotal: {producto['subtotal']:,}")
    total_cliente += producto['subtotal']
    print(f"Total a pagar: {total_cliente:,}\n")
    total_general += total_cliente
    if total_general == 0:
        print("No hubo pedidos")
        input("Presiona ENTER para continuar...")
    else:
        print(f"Total recaudado por la tiendita: ${total_general:,}")
