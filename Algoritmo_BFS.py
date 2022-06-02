from queue import Queue

class Grafo:
     # Constructor
    def __init__(self, numero_de_nodos, direccion=True):
        self.numero_de_nodos= numero_de_nodos
        self.nodos = range(self.numero_de_nodos)
		
        # Direccion
        self.direccion = direccion
		
       # Representación gráfica - Lista de adyacencia
        # Usamos un diccionario para implementar una lista de adyacencia
        self.lista_adyaciencia = {nodo: set() for nodo in self.nodos} 
    
    # Agregar borde al gráfico
    def agregar_borde(self, nodo1, nodo2, peso=1 ):
        self.lista_adyaciencia[nodo1].add((nodo2, peso))

        if not self.direccion:
            self.lista_adyaciencia[nodo2].add((nodo1, peso))
    
     # Imprimir la representacion grafica
    def Mostrar_lista_adyaciencia(self):
        for llave in self.lista_adyaciencia.keys():
            print("Nodo", llave, ": ", self.lista_adyaciencia[llave])

        # Función que imprime el recorrido BFS
    # de un vértice fuente dado. bfs_transversal(int s)
    # atraviesa vértices alcanzables desde s.
    def recorrido(self, iniciar_nodo):
       # Conjunto de nodos visitados para evitar bucles
        visitado = set()
        cola = Queue()

       ## Agregue start_node a la cola y la lista visitada
        cola.put(iniciar_nodo)
        visitado.add(iniciar_nodo)

        while not cola.empty():
           # Desencolar un vértice hacer cola e imprimirlo
            nodo_actual = cola.get()
            print( nodo_actual, end= " ")

            # Obtener todos los vértices adyacentes del
            # vértice desencolado. Si un adyacente
            # no ha sido visitado, luego márcalo
            # visitado y ponerlo en cola
            for (siguiente_nodo, peso) in self.lista_adyaciencia[nodo_actual]:
                if siguiente_nodo not in visitado:
                    cola.put(siguiente_nodo)
                    visitado.add(siguiente_nodo)