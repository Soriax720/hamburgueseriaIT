import time

def tomar_pedido():
   cliente = input("Ingrese nombre del cliente: ")
   cant_s = int(input("Ingrese cantidad Combo S: "))
   cant_d = int(input("Ingrese cnatidad Combo D: "))
   cant_t = int(input("Ingrese cantidad Combo T: "))
   cant_p  = int(input("Ingrese cantidad Flurby: "))

   total = (
       cant_s * COMBO_SIMPLE + 
       cant_d * COMBO_DOBLE + 
       cant_t * COMBO_TRIPLE + 
       cant_p * POSTRE)
   print(f"Total: ${total}")
   pago = int(input("Abona con $ "))
   diferencia = pago - total
   if diferencia > 0:
       print(f"Vuelto: ${diferencia}")
   elif diferencia == 0:
       print(f"Pago exacto")
   else:
       print(f"Falta pagar: ${-diferencia}")
   
   confirmacion = input("¿Confirma peido? Y/N: ")
   if confirmacion == "Y" or confirmacion == "y":
       with open("ventas.txt", "a") as f:
        fecha_actual = time.ctime()
        linea_venta = f"{cliente};{fecha_actual};{cant_s};{cant_d};{cant_t};{cant_p};{total}\n"
        f.write(linea_venta)


COMBO_SIMPLE = 5
COMBO_DOBLE = 6
COMBO_TRIPLE = 7
POSTRE = 2

print("Bienvenido a Hamburguesa IT")
encargado = input("Ingrese su nombre encargado: ")
while True:
    print("\n--- Hambuerguesas IT")
    print(f"Encargado --> {encargado}")
    print("1 - Ingreso nuevo pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar sistema")
    
    opcion = int(input("Eliga una opcion: "))
    if opcion == 1:
       tomar_pedido()
    elif opcion == 2:
       encargado = input("Ingrese su nombre encargado: ")
    elif opcion == 3:
       print("Apagando sistema...")
       break
    else:
       print("Opcion invalida")