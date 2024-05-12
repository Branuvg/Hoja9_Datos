# Hoja de trabajo 9
# Gabriel Bran - 23590
# Luis Padilla - 23663

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