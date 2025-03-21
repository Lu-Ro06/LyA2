from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial) 
    nodos_frontera.append(nodoInicial)

    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)  
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo 

        dato_nodo = nodo.get_datos()


        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]], nodo)
        if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_derecho)

        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]], nodo)
        if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_central)

        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]], nodo)
        if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_izquierdo)

    return None  

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() is not None: 
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        print(resultado)