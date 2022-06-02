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