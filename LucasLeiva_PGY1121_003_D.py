#BIBLiOTECA-----------------------------------------------------------------------
import random as r
import os
import time
import msvcrt as m
import numpy as np

def limpia_pantalla(seg):
   time.sleep(seg)
   os.system("cls")
   
#PATINUM---------------------------------------------------------------------------
num_platinum = list(range(0,21))
cant_platinum = 0
monto_platinum = 0
#GOLD------------------------------------------------------------------------------
num_gold = list(range(21,51))
cant_gold = 0
monto_gold = 0
#SILVER----------------------------------------------------------------------------
num_silver = list(range(51,101))
cant_silver = 0
monto_silver = 0

puesto = []
asistentes = []
#Filas asiento de Escenario--------------------------------------------------------
cont=1
for i in range(10):
    puesto_escenario=[]
    for j in range(10):
        puesto_escenario.append(cont)
        cont += 1
    puesto.append(puesto_escenario)

#DEFINICIONES----------------------------------------------------------------------
def menu():
    print("--------------------------------")
    print("[         Creativos.CL         ]")
    print("--------------------------------")
    print("--------------Menú--------------")
    print("[1.- Comprar Entradas          ]")
    print("[2.- Mostrar sitios Disponibles]")
    print("[3.- Ver listado asistentes    ]")
    print("[4.- Mostrar ganancias totales ]")
    print("[0.- Salir                     ]")
    print("--------------------------------")
    op=int(input("Seleccione la opcion que desea:   "))
    return op

def escene():
    print("--------------------")
    print("     ESCENARIO      ")
    print("--------------------")
    for fila in puesto:
        print(fila)

def salir():
    limpia_pantalla(0)
    print(f"Gracia por su compra! Fecha de la Compra: {time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year}")
    print("Saliendo del Sistema...")
    limpia_pantalla(1)
    for i in range (3,0,-1):
        print(f"Saliendo en {i}")
        limpia_pantalla(2)

def buy_chair(asiento):
    global cant_platinum
    global monto_platinum
    global cant_gold
    global monto_gold
    global cant_silver
    global monto_silver

    if asiento in num_platinum:
        cant_platinum=cant_platinum+1
        monto_platinum=monto_platinum+120000
    elif asiento in num_gold:
        cant_gold = cant_gold + 1
        monto_gold = monto_gold + 80000
    elif asiento in num_silver:
        cant_silver = cant_silver + 1
        monto_silver = monto_silver + 50000  

def ganancias():
    print("--------------------------")
    print("| \tGanancias\t |")
    print("--------------------------")

    print("Platinum")
    print("Cantidad: ", cant_platinum)
    print("Monto: ", monto_platinum)
    print("--------------------------")
    print("Gold")
    print("Cantidad: ", cant_gold)
    print("Monto: ", monto_gold)
    print("--------------------------")
    print("Silver")
    print("Cantidad: ", cant_silver)
    print("Monto: ", monto_silver)
    print("---------------------------------------")
    total=monto_gold+monto_platinum+monto_silver
    print(f"GANANCIAS TOTALES = {total}")
    print("---------------------------------------")
    print("Presione cualquier tecla para continuar")
    m.getch()
    limpia_pantalla(1)

def marca_de_ocupado(asiento):
    for a,i in enumerate(puesto):
        for b,j in enumerate(i):
            if j==asiento:
                puesto[a][b]='X'

def asiento_ocupado(num):
    cont=1
    sw=0
    for fila in puesto:
        if(num in fila):
            sw=1

    if not sw:
        print("* Este asiento no esta Disponible *")
        return True
    for i in puesto:
        for j in i:
            if cont==num and j == 'X':
                return True
 
    return False

def entradas():
    print("Cargando...")
    limpia_pantalla(1)
    cant_entradas=int(input("Ingrese cuantas entradas desea Comprar:    "))
    minimo=1
    maximo=3

    while (cant_entradas<minimo or cant_entradas>maximo):
        cant_entradas=int(input("Debe de ingresar una cantidad valida por el sistema (1 a 3 entradas)\t"))
    
    escene()

    for i in range(cant_entradas):
        print("")
        asiento=int(input("Ingrese el Numero del asiento que desea:     "))
        while asiento_ocupado(asiento):
            asiento=int(input("Ingrese el numero de asiento que desea:  "))
        marca_de_ocupado(asiento)
        buy_chair(asiento) 
    while True: 
        rut_asistente=input("Ingrese su rut(SOLO NUMEROS):  ")
        if len(rut_asistente)==9 and rut_asistente.isdigit:
            break
        else:
            print("Ingrese un rut valido de 9 digitos")

    asistentes.append(rut_asistente)
    print("Entradas Compradas con Exito!")
    limpia_pantalla(2)
    print("Presione cualquier tecla para continuar")
    m.getch()
    limpia_pantalla(0)

def listado_asistentes():
    print("--------------------------")
    print("|\tASISTENTES\t|")
    print("--------------------------")
    for asistente in asistentes:
        print (asistente)
        print("--------------------------")
    print("---------------------------------------")
    print("Presione cualquier tecla para continuar")
    m.getch()
    limpia_pantalla(1)



#PROGRAMA PRINCIPAL-------------------------------------------------------------------
while True:
    try:
        opcion=menu()
        if opcion==1:
            entradas()
        elif opcion==2:
            escene()
        elif opcion==3:
            listado_asistentes()
        elif opcion==4:
            ganancias()
        elif opcion==0:
            salir()
        else:
            print("Selecciona una Opcion Valida")
            limpia_pantalla(1)
    except:
        print("¡OH NO! ha ocurrido un Error :( ")