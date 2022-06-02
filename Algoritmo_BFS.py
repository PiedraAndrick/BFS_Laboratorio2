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