# Hoja de trabajo 9
# Gabriel Bran - 23590
# Luis Padilla - 23663

import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Hace el menu para que el usuario pueda ver sus opciones
def menu():
    while True:
        print("Bienvenido al Menu de Rutas para buses")
        print("1. Mostrar rutas establecidas")
        print("2. Mostrar grafico")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            muestra_salidas()
        elif opcion == '2':
            muestra_grafico(rutas)
        elif opcion == '3':
            print("Gracias por utilizar el programa de buses.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# muestra las opciones de lugares de salidas
def muestra_salidas():
    while True:
        print("Opcion de Rutas: Escribe el nombre de la ruta la cual quisieras saber.")
        print("- Pueblo Paleta")
        print("- Aldea Azalea")
        print("- Ciudad Safiro")
        print("- Aldea Fuego")
        print("- Ciudad Lavanda")

        ver = input("Escriba una opcion: ").lower()

        if ver == "pueblo paleta":
            muestra_rutas(rutas, 'Pueblo Paleta')
            break
        elif ver == 'aldea azalea':
            muestra_rutas(rutas,'Aldea Azalea')
            break
        elif ver == 'ciudad safiro':
            muestra_rutas(rutas,'Ciudad Safiro')
            break
        elif ver == 'aldea fuego':
            muestra_rutas(rutas, 'Aldea Fuego')
            break
        elif ver == 'ciudad lavanda':
            muestra_rutas(rutas, 'Ciudad Lavanda')
            break
        else:
            print("Ruta no econtrada, escribe una ruta valida")

# abre el archivo para leerlo
rutas = {}
archivo = "rutas.txt"
with open(archivo, 'r') as file:
    for line in file:
        line = line.replace('"', '')
        salida, destino, costo = line.strip().split(', ')
        costo = int(costo)
        rutas.setdefault(salida, {})[destino] = costo
        rutas.setdefault(destino, {})[salida] = costo

# Genera la grafica
def muestra_grafico(rutas):
    N = nx.Graph()
    for estacion in rutas.keys():
        N.add_node(estacion)
    for salida, destinos in rutas.items():
        for destino, costo in destinos.items():
            N.add_edge(salida, destino, weight=costo)
    nx.draw(N, with_labels=True, node_color="green", node_size=2000)
    plt.margins(0.1)
    plt.show()

# Algoritmo Dijkstra
def alg_dij(rutas, inicio):
    distancias = {nodo: float('inf') for nodo in rutas}
    rutas_completadas = {nodo: [] for nodo in rutas}
    distancias[inicio] = 0
    priority_Queue = [(0, inicio)]
    while priority_Queue:
        distancia_actual, node_actual = heapq.heappop(priority_Queue)
        for vecino, costo_De_Vecino in rutas[node_actual].items():
            distancia_actualizada = distancia_actual + costo_De_Vecino
            if distancia_actualizada < distancias[vecino]:
                distancias[vecino] = distancia_actualizada
                rutas_completadas[vecino] = rutas_completadas[node_actual] + [node_actual]
                heapq.heappush(priority_Queue, (distancia_actualizada, vecino))
    return distancias, rutas_completadas

# muestra las rutas disponibles por salidas
def muestra_rutas(rutas, inicio):
    distancias, rutas_completas = alg_dij(rutas, inicio)
    print(f"\nDesde '{inicio}':")
    for destino, costo in distancias.items():
        if destino != inicio:
            if costo < float('inf'):
                print(f" - Hasta {destino}, Costo: {costo}")
            else:
                break

# Ejecucion de todo el programa
menu()