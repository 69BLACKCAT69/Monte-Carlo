import random
import time

def guardar_en_archivo(numeros):
    with open("numeros.txt", "w") as archivo:
        for numero in numeros:
            archivo.write(str(numero) + "\n")
    return

def verificar_condiciones(x0, t, p, a, m, c):
    # Condición 1: x0 debe ser un número entero impar no divisible entre 2 y 5
    condicion_1 = x0 % 2 != 0 and x0 % 5 != 0
    
    # Condición 2: c debe ser un entero impar relativamente primo a m
    def determinar_relativamente_primos(c, m):
        factores_num1 = [i for i in range(1, c+1) if c % i == 0]
        factores_num2 = [i for i in range(1, m+1) if m % i == 0]
        factores_comunes = [factor for factor in factores_num1 if factor in factores_num2]
        
        if len(factores_comunes) == 1 and 1 in factores_comunes:
            return True
        else:
            return False
    condicion_2 = determinar_relativamente_primos(c, m)

    return condicion_1 and condicion_2

# Generar números pseudoaleatorios hasta que todas las condiciones se cumplan
def valores():

    while True:
        x0 = random.randint(1, 100)  # Genera x0 aleatoriamente
        
        t = random.randint(1, 100)  # Genera t aleatoriamente
        p = random.choice([3, 11, 13, 19, 21, 27, 29, 37, 53, 59, 61, 67, 69, 77, 83, 91])  # Elige p aleatoriamente de un elemento en una lista
        A = random.randint(0, 1)  # Genera la decisión si va ser - o + aleatoriamente para generar a
        d = (random.randint(1, 4))  #   Genera m aleatoriamente
        m = 10**d
        c = random.randint(1, 100)  # Genera c aleatoriamente

        if A == 0:
            a = (200*t) + p
        else:
            a = (200*t) - p

        if verificar_condiciones(x0, t, p, a, m, c):
            return x0, a, t, p, d, m, c
    
def generador_numeros_pseudoaleatorios(x0, a, t, p, exponente, m, c, cantidad=None, periodo=None):
    numeros_generados = []
    x_condicion = x0

    if opcion==1:
        cantidad = int(input("Ingrese la cantidad de números pseudoaleatorios: "))

        while cantidad > 0:
            xn = ((a * x0) + c) % m
            numero_pseudoaleatorio = xn / m
            if int(numero_pseudoaleatorio*100)>=1:
                numeros_generados.append(numero_pseudoaleatorio)
            else:
                cantidad+=1
            x0 = xn
            cantidad -=1
            
        print("Números pseudoaleatorios generados:")
        for indice, numero in enumerate(numeros_generados):
            if xn >= 0 and xn <= m:
                print(indice+1, " - ", numero)
            else:
                print("Hubo un error")

    elif opcion==2:
        while True:
            xn = ((a * x0) + c) % m
            numero_pseudoaleatorio = xn / m
            numeros_generados.append(numero_pseudoaleatorio)
            if xn == x_condicion:
                break
            else:
                x0 = xn
        
        print("Números pseudoaleatorios generados:")
        for indice, numero in enumerate(numeros_generados):
            if xn >= 0 and xn <= m:
                print(indice+1, " - ", numero)
                time.sleep(periodo)
            else:
                print("Hubo un error")
    
    return numeros_generados  # Agrega un valor de retorno

while True: 
    
    x0, a, t, p, exponente, m, c = valores()

    print("La semilla es: ", x0)
    print("valor de t: ", t)
    print("valor de p: ", p)
    print("El valor de a es: ", a)
    print("El valor del exponente: ", exponente)
    print("El valor de m es: ", m)
    print("El valor de c es: ", c)
    print("--------------------------------")

    print("Seleccione una opción: ")
    print("1: Generar por cantidad")
    print("2: Generar por período")
    opcion = int(input("Opción: "))

    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad de números pseudoaleatorios: "))
        numeros_generados = generador_numeros_pseudoaleatorios(x0, a, t, p, exponente, m, c, cantidad=cantidad)
        guardar_en_archivo(numeros_generados)  # Llama a guardar_en_archivo después de generar los números
    elif opcion == 2:
        periodo = float(input("Ingrese el período en segundos entre cada número pseudoaleatorio: "))
        numeros_generados = generador_numeros_pseudoaleatorios(x0, a, t, p, exponente, m, c, periodo=periodo)
        guardar_en_archivo(numeros_generados)  # Llama a guardar_en_archivo después de generar los números
    else:
        print("Opción no válida")

    otra_vez = input("Desea volver a generar otros numeros aleatorios (si/no): ")
    print("-------------------------------------------------------------------")
    print(" ")
    if otra_vez == "si" or otra_vez == "s" or otra_vez == "SI":
        continue
    else:
        break

