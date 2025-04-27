import os
#Definimos la función decimal a binario
def decimal_a_binario(num):
    """
    13|2
    6|1
    3|0
    1|1
    13|2
    |1
    %

    """
    if num == 0:
        return "0"
    #Tomamos el valor absoluto del número ingresado
    decimal = abs(num)
    binario = ""

    while decimal > 0:
        binario = str(decimal%2) + binario
        decimal = decimal // 2

    if num < 0:
        #Agregamos el signo negativo delante del número binario
        return ("-" + binario)
    else:
        return binario
    
#Definimos la función binario a decimal 
def binario_a_decimal(numbin):
    """

    1011
    1*2^3 + 0*2^2 + 1*2^1 + 1*(2^0)
    i = 0,1,2,3
    bit = 1,1,0,1
    """
#Se le agrega el signo negativo delante del número
    negativo = numbin.startswith('-')

    if negativo:
        numbin = numbin[1:]

    decimal = 0

    for i in range(len(numbin)):
        bit = int(numbin[-(i+1)])
        decimal += bit*(2**i)

    return -decimal if negativo else decimal

def es_binario(numbin):
    if numbin.startswith('-'):
        numbin = numbin[1:]
    return all(c in '01' for c in numbin)

def es_decimal(numstr):
    if numstr.startswith('-'):
        numstr = numstr[1:]
    return numstr.isdigit()

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
#Definimos la función menu para que el usuario seleccione que función quiere convertir
def menu():
    while True:
        limpiar_pantalla()
        print("=== CONVERSOR BINARIO / DECIMAL ===")
        print("1. Decimal a Binario")
        print("2. Binario a Decimal")
        print("3. Salir")
        opcion = input("Elegí una opción (1-3): ")
#Desde esta sección aparecen las distintas opciones que puede seleccionar el usuario
        if opcion == "1":
            numstr = input("Ingresá un número decimal: ")
            if es_decimal(numstr):
                num = int(numstr)
                print(f"Binario: {decimal_a_binario(num)}")
            else:
                print("Entrada inválida. Debe ser un número entero.")
        
        elif opcion == "2":
            numbin = input("Ingresá un número binario: ")
            if es_binario(numbin):
                print(f"Decimal: {binario_a_decimal(numbin)}")
            else:
                print("Entrada inválida. Debe contener solo 0 y 1.")
        
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Elegí 1, 2 o 3.")

        input("\nPresioná Enter para continuar...")
menu()