import time
import os
from database import GestionBaseDatos

db = GestionBaseDatos()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def tomar_pedido():
   cliente = input("Ingrese nombre del cliente: ")
   cant_s = leer_entero("Ingrese cantidad Combo S: ")
   cant_d = leer_entero("Ingrese cantidad Combo D: ")
   cant_t = leer_entero("Ingrese cantidad Combo T: ")
   cant_p  = leer_entero("Ingrese cantidad Combo P: ")

   total = (
       cant_s * COMBO_SIMPLE + 
       cant_d * COMBO_DOBLE + 
       cant_t * COMBO_TRIPLE + 
       cant_p * POSTRE)
   print(f"Total: ${total}")
   
   pago = leer_entero("Abona con $ ")
   diferencia = pago - total
   if diferencia > 0:
       print(f"Vuelto: ${diferencia}")
   elif diferencia == 0:
       print(f"Pago exacto")
   else:
       print(f"Falta pagar: ${-diferencia}")
   
   confirmacion = input("¿Confirma peido? Y/N: ")
   if confirmacion == "Y" or confirmacion == "y":
       fecha_venta = time.ctime()
       db.insertar_venta(cliente, fecha_venta, cant_s, cant_d, cant_t, cant_p, total)
       return total
   else:
      return 0

def registrar_evento(tipo, nombre_enc, monto = 0):
    fecha_act = time.ctime()
    db.insertar_registro(nombre_enc, fecha_act, tipo, monto)

def leer_entero(mensaje):
   while True:
      try:
         return int(input(mensaje))
      except ValueError:
         print("Error: Por favor, ingrese un número entero.")

COMBO_SIMPLE = 5
COMBO_DOBLE = 6
COMBO_TRIPLE = 7
POSTRE = 2

print("Bienvenido a Hamburguesa IT")
encargado = input("Ingrese su nombre encargado: ")
monto_acumulado = 0
registrar_evento("IN", encargado)



while True:
    print("\n--- Hambuerguesas IT")
    print(f"Encargado --> {encargado}")
    print("1 - Ingreso nuevo pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar sistema")
    
    opcion = leer_entero("Elija una opcion: ")

    if opcion == 1:
         limpiar_pantalla()
         resultado_venta = tomar_pedido()
         monto_acumulado += resultado_venta
    elif opcion == 2:
      limpiar_pantalla()
      registrar_evento("OUT", encargado, monto_acumulado)
      monto_acumulado = 0   
      encargado = input("Ingrese su nombre encargado: ")
      registrar_evento("IN", encargado, monto_acumulado)   
    elif opcion == 3:
         limpiar_pantalla()
         registrar_evento("OUT", encargado, monto_acumulado)
         print("Apagando sistema...")
         break
    else:
         print("Opcion invalida")
   
      