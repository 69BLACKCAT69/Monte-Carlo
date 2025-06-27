import pandas as pd
from rich.table import Table
from rich.console import Console
from datetime import datetime, timedelta#utiliza para representar fechas y horas concretas

# Lee el archivo de Excel
num = pd.read_excel(r"Tiempo_Llegada.xlsx")
num2 = pd.read_excel(r"Tiempo_Servicio.xlsx")

# Convierte los datos en una lista de listas y Filtra las filas que no son la última fila (que contiene el total)
tabla_llegada = num[:-1].values.tolist()#los alamacena en una lista para poder manejar las filas y columnas de la tabla
tabla_servicio = num2[:-1].values.tolist()

def Tiempo_Servicios():
    try:
        global intervalos, guarda_tiempo_servicio
        ###################################### TIEMPO DE SERVICIO #####################################
        print("TIEMPO DE SERVICIO")

        suma_total = 0
        for a in tabla_servicio:
            suma_total += a[1]

        print("Paso 1 ")
        tabla1 = Table()
        tabla1.add_column("Tiempo de Servicio en minutos")
        tabla1.add_column("Frecuencia")

        for fila in tabla_servicio:
            tabla1.add_row(f"{fila[0]}",f"{fila[1]}")
            
        console.print(tabla1)

        tabla2 = Table()
        tabla2.add_column("Tiempo de Servicio en minutos")
        tabla2.add_column("Frecuencia")
        tabla2.add_column("Probabilidad de ocurrencia")
        tabla2.add_column("Probabilidad de ocurrencia")


        for fila in tabla_servicio:
            tabla2.add_row(f"{fila[0]}",f"{fila[1]}",f"{fila[1]}/{suma_total}",f"{fila[1]/suma_total}")

        console.print(tabla1)

        print("Paso 2 ")
        table3 = Table()#se crea la tabla
        table3.add_column("Tiempo de Servicio en minutos")
        table3.add_column("Frecuencia")
        table3.add_column("Probabilidad de ocurrencia")
        table3.add_column("Probabilidad de ocurrencia")
        table3.add_column("Probabilidad de ocurrencia acumulado")

        prob_ocu_acu = 0

        for fila in tabla_servicio:
            prob_ocu_acu += fila[1]/suma_total#almacena los valores
            table3.add_row(f"{fila[0]}",f"{fila[1]}",f"{fila[1]}/{suma_total}",
                           f"{fila[1]/suma_total}",f"{prob_ocu_acu:.2f}")
            #para que nos de la suma de numeros en la suma

        console.print(table3)

        print("Paso 3 ")
        table4 = Table()
        table4.add_column("Tiempo de Servicio en minutos")
        table4.add_column("Frecuencia")
        table4.add_column("Probabilidad de ocurrencia")
        table4.add_column("Probabilidad de ocurrencia")
        table4.add_column("Probabilidad de ocurrencia acumulado")
        table4.add_column("Intervalo de numeros aleatorios")

        prob_ocu_acu = 0
        interv_ini = 0
        intervalos = []

        for fila in tabla_servicio:
            prob_ocu_acu += fila[1]/suma_total#para almacenar los valores
            table4.add_row(f"{fila[0]}",f"{fila[1]}",f"{fila[1]}/{suma_total}",f"{fila[1]/suma_total}",
                        f"{prob_ocu_acu:.2f}",f"{interv_ini*100+1:.0f} a {prob_ocu_acu*100:.0f}")
            intervalos.append([fila[0], f"{interv_ini*100+1:.0f}", f"{prob_ocu_acu*100:.0f}"])
            #numeros de probabilidad por el numero de clientes y su respectivo aumento
            interv_ini=prob_ocu_acu#se actualiza los valores

        console.print(table4)

        guarda_tiempo_servicio = []

        print("PASO 4 ")
        tabla5 = Table()
        tabla5.add_column("CLIENTES ")
        tabla5.add_column("NUMERO ALEATORIOS ")
        tabla5.add_column("INTERVALO ENTRE LLEGADAS ")
        tabla5.add_column("INTERVALO ")
                    
        for a in range(clientes):
            for inter in intervalos:
                if int(inter[1]) <= int(numeros[a]*100) <= int(inter[2]):
                    guarda_tiempo_servicio.append(inter[0])
                    tabla5.add_row(f"{a+1}",f"{int(numeros[a]*100)}",f"{inter[0]}",f"{int(inter[1])} a {int(inter[2])}")
        
        console.print(tabla5)

    except Exception:
        print("Hubo un posible error en los numeros pseudaleatorios o faltan mas numeros pseudoaleatorios")
        print("Favor de revisar el documento de texto de los numeros ")
        print()

def Tiempo_llegada(): #funcion 2
    try:
        global intervalos2, guarda_tiempo_llegada
        ######################################################### TABLA DE LLEGADA #####################################################       
        print("TIEMPO DE LLEGADA")
        
        suma_total = 0
        for a in tabla_llegada:
            suma_total += a[1]#acumulador

        print("Paso 1 ")
        table6 = Table()
        #TABLA DE TIEMPO DE LLEGADAS
        table6.add_column("Tiempo de llegadas en minutos")
        table6.add_column("Frecuencia")

        for fila in tabla_llegada:
            table6.add_row(f"{fila[0]}",f"{fila[1]}")
            
        console.print(table6)

        table7 = Table()
        table7.add_column("Tiempo de llegadas en minutos")
        table7.add_column("Frecuencia")
        table7.add_column("Probabilidad de ocurrencia")
        table7.add_column("Probabilidad de ocurrencia")

        for fila in tabla_llegada:
            table7.add_row(f"{fila[0]}",f"{fila[1]}",f"{fila[1]}/{suma_total}",f"{fila[1]/suma_total}")

        console.print(table7)

        print("Paso 2 ")
        table8 = Table()
        table8.add_column("Tiempo de llegadas en minutos")
        table8.add_column("Frecuencia")
        table8.add_column("Probabilidad de ocurrencia")
        table8.add_column("Probabilidad de ocurrencia")
        table8.add_column("Probabilidad de ocurrencia acumulado")

        prob_ocu_acu = 0

        for fila in tabla_llegada:
            prob_ocu_acu += fila[1]/suma_total
            table8.add_row(f"{fila[0]}",f"{fila[1]}",f"{fila[1]}/{suma_total}",f"{fila[1]/suma_total}",f"{prob_ocu_acu:.2f}")

        console.print(table8)

        print("Paso 3 ")
        table9 = Table()
        table9.add_column("Tiempo de llegadas en minutos")
        table9.add_column("Frecuencia")
        table9.add_column("Probabilidad de ocurrencia")
        table9.add_column("Probabilidad de ocurrencia")
        table9.add_column("Probabilidad de ocurrencia acumulado")
        table9.add_column("Intervalo de numeros alaeatorios")


        prob_ocu_acu = 0
        interv_ini = 0
        intervalos2 = []

        for fila in tabla_servicio:
            prob_ocu_acu += fila[1]/suma_total
            table9.add_row(f"{fila[0]}",f"{fila[1]}",f"{fila[1]}/{suma_total}",f"{fila[1]/suma_total}",
                        f"{prob_ocu_acu:.2f}",f"{interv_ini*100+1:.0f} a {prob_ocu_acu*100:.0f}")
            intervalos2.append([fila[0], f"{interv_ini*100+1:.0f}", f"{prob_ocu_acu*100:.0f}"])
            interv_ini=prob_ocu_acu

        console.print(table9)

        guarda_tiempo_llegada = []

        print("PASO 4 ")
        tabla10 = Table()
        tabla10.add_column("CLIENTES ")
        tabla10.add_column("NUMERO ALEATORIOS ")
        tabla10.add_column("INTERVALO ENTRE LLEGADAS ")
        tabla10.add_column("INTERVALO ")
                    
        for a in range(clientes):
            for inter in intervalos2:#se van a checar  todos los intervalos
                if int(inter[1]) <= int(numeros[clientes+a]*100) <= int(inter[2]):#mayor igual<=
                    #lo que hace cheque si esta en medio de los dos numeros
                    guarda_tiempo_llegada.append(inter[0])#guardar el numero de los minutos
                    tabla10.add_row(f"{a+1}",f"{int(numeros[clientes+a]*100)}",f"{inter[0]}",
                                    f"{int(inter[1])} a {int(inter[2])}")
                
        console.print(tabla10)

    except Exception:#no cumpla un intervalo y marca error
        print("Hubo un posible error en los numeros pseudaleatorios o faltan mas numeros pseudoaleatorios")
        print("Favor de revisar el documento de texto de los numeros ")
        print()

def Tabla_Final():
    try:
        # Asumiendo que tienes definidos los valores de guarda_tiempo_llegada,
        # guarda_tiempo_servicio, hora, minuto y clientes
        print("TABLA FINAL")
        print("PASO 5")
        tabla_final = Table()
        tabla_final.add_column("CLIENTE ")
        tabla_final.add_column("NUMERO ALEATORIOS ")
        tabla_final.add_column("INTERVALO DE LLEGADA ")
        tabla_final.add_column("NUMERO ALEATORIOS ")
        tabla_final.add_column("INTERVALO DE SERVICIO ")
        tabla_final.add_column("HORA DE LLEGADA ")
        tabla_final.add_column("HORA DE SERVICIO ")
        tabla_final.add_column("HORA DE SALIDA ")
        tabla_final.add_column("TIEMPO DE ESPERA ")
        tabla_final.add_column("TIEMPO EN EL SISTEMA ")


        """
        datetime se utiliza para representar fechas y horas concretas

        timedelta se utiliza para representar la diferencia o duración entre dos fechas/horas,
        permitiendo operaciones aritméticas con ellas (suma/resta).

        strftime('%H:%M') toma un objeto datetime y 
        devuelve una cadena de texto que representa esa fecha y hora en formato de 24 horas, 
        separando las horas y minutos por dos puntos.
        """

        hora_llegada = datetime(year=2023, month=1, day=1, hour=hora, minute=minuto)
        hora_servicio = hora_llegada#para iniciar los valores por el momento
        hora_salida = hora_llegada

        tiempo_espera_total = 0#acumuladores del sistema y para que imprima hasta el final
        tiempo_en_sistema_total = 0
        tiempo_servicio_total = 0

        for a in range(clientes):
            hora_llegada += timedelta(minutes=guarda_tiempo_llegada[a])#convertir el tiempo en la lista en minutos
            #operaciones
            #print(hora_llegada,timedelta(minutes=guarda_tiempo_llegada[a]))
            #se almacena a la hora_llegada
            if a == 0:#primer cliente
                hora_servicio = hora_llegada

            # Caso no se esta atendiendo a nadie hasta que llegue un cliente
            if hora_llegada > hora_servicio:#mayor
                #la hora de hora de servicio se actualice con forma ese cliente llego
                hora_servicio = hora_llegada

            hora_salida = hora_servicio + timedelta(minutes=guarda_tiempo_servicio[a])
            #La hora de la salida del sistema

            #Me arroja la diferencia entre segundos y se divide entre 60 para poder obtenerla en minutos
            tiempo_espera = (hora_servicio - hora_llegada).total_seconds() / 60  
            # Cálculo del tiempo de espera para darnos el tiempo en minutos
            tiempo_en_sistema = (hora_salida - hora_llegada).total_seconds() / 60 
            # Cálculo del tiempo en el sistema

            tiempo_espera_total += tiempo_espera
            tiempo_en_sistema_total += tiempo_en_sistema
            tiempo_servicio_total += + guarda_tiempo_servicio[a]#acumulando los valores
            
            # strftime('%H:%M') toma un objeto datetime y 
            #devuelve una cadena de texto que representa esa fecha y hora en formato de 24 horas, 
            #separando las horas y minutos por dos puntos.
            tabla_final.add_row(
                f"{a + 1}",#
                f"{int(numeros[clientes+a] * 100)}",#
                f"{guarda_tiempo_llegada[a]}",#
                f"{int(numeros[a] * 100)}",#
                f"{guarda_tiempo_servicio[a]}",#
                f"{hora_llegada.strftime('%H:%M')}",#
                f"{hora_servicio.strftime('%H:%M')}",#
                f"{hora_salida.strftime('%H:%M')}",#
                f"{tiempo_espera} min",#
                f"{tiempo_en_sistema} m",#para insertar los datos en la tabla
            )

            hora_servicio = hora_salida
        
        console.print(tabla_final)

        print("Tiempo Promedio Dentro Del Sistema: ",tiempo_en_sistema_total/clientes)
        print("Tiempo Promedio De Espera Total: ",tiempo_espera_total/clientes)
        print("Tiempo Promedio De Servicio Total: ",tiempo_servicio_total/clientes)

    except Exception as e:
        print(f"Error: {e}")
    
console = Console()#1

clientes = int(input("Dame el numero de clientes que se va a simular: "))
hora = int(input("Dame el numero de la hora en el que la empresa abre: "))
minuto = int(input("Dame el numero en minuto en el que la empresa abre: "))

while True:
    if 0<=hora<=23 and 0<=minuto<=59:
        break
    else:
        print("ERROR - La Hora O Los Minutos Esta Mal Insertado ")
        hora = int(input("Dame el numero de la hora en el que la empresa abre: "))
        minuto = int(input("Dame el numero en minuto en el que la empresa abre: "))

def leer_numeros():
    with open('numeros.txt', 'r') as archivo:
        return [float(num.strip()) for num in archivo]

numeros = leer_numeros()#funcion1

Tiempo_Servicios()#funcion2
Tiempo_llegada()#funcion3
Tabla_Final()#funcion4
