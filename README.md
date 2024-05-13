# Hoja9_Datos
# Algoritmo de Dijkstra para encontrar la ruta más corta.
Este código implementa el algoritmo de Dijkstra en Python para encontrar la ruta más corta entre diferentes lugares para un sistema de buses de parte de la hoja de trabajo 9.

# Instrucciones de uso:
- Selecciona una opción 1 para ver que ralación de salida y destino tiene cada una de las ciudades que se muestran, 2 para los graficos y 3 para salir.

# Cómo funciona:
- Lectura del archivo de rutas: El programa lee un archivo llamado "rutas.txt" que contiene información sobre las rutas disponibles. Cada línea del archivo representa una conexión entre dos lugares y su respectivo costo. La información se almacena en un diccionario llamado rutas.
- Algoritmo de Dijkstra: Se implementa el algoritmo de Dijkstra para encontrar las rutas más cortas y sus respectivos costos desde un punto de inicio dado hacia todos los demás destinos disponibles. La función alg_dij toma como entrada el diccionario de rutas y el lugar de inicio, y devuelve las distancias mínimas y las rutas completas desde el lugar de inicio hacia todos los demás destinos. 
- Generación de gráfico: La función muestra_grafico utiliza la biblioteca NetworkX para generar un gráfico de las rutas disponibles. Cada lugar se representa como un nodo en el gráfico, y las conexiones entre lugares se representan como bordes. Los costos de las rutas se muestran como pesos en los bordes. 
- Menú de opciones: Se proporciona un menú de opciones al usuario para interactuar con el programa. Las opciones incluyen mostrar las rutas establecidas, mostrar el gráfico de las rutas y salir del programa. 
- Funciones de visualización de rutas: Las funciones muestra_salidas y muestra_rutas permiten al usuario seleccionar un lugar de salida y ver las rutas disponibles desde ese lugar. La función muestra_rutas utiliza el algoritmo de Dijkstra para calcular las rutas más cortas y sus costos desde el lugar de inicio seleccionado.


# Estructura del proyecto:
- `main.py`: Contiene el código Python.
- `rutas.txt`: Archivo que contiene las rutas.
- `README.md`: Este archivo, que proporciona instrucciones de la Hoja