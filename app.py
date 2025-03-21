from flask import Flask, request, render_template
from arbol import Nodo
from DFS_rec import buscar_solucion_dfs_rec
from puzzle import buscar_solucion_BFS
from lifo import buscar_solucion_DFS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Procesar los datos del formulario
        estado_inicial = list(map(int, request.form['estado_inicial'].split(',')))
        solucion = list(map(int, request.form['solucion'].split(',')))
    except ValueError:
        return "Los valores de 'estado_inicial' y 'solucion' deben ser números separados por comas.", 400

    # Inicializar un diccionario para los resultados
    resultados = {}

    # Resolver usando DFS recursivo
    resultado_dfs = []
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_dfs = buscar_solucion_dfs_rec(nodo_inicial, solucion, visitados)
    if nodo_dfs:
        nodo_actual = nodo_dfs
        while nodo_actual.get_padre() is not None:
            resultado_dfs.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        resultado_dfs.append(nodo_actual.get_datos())
        resultado_dfs.reverse()
    resultados['DFS'] = resultado_dfs

    # Resolver usando BFS
    resultado_bfs = []
    nodo_bfs = buscar_solucion_BFS(estado_inicial, solucion)
    if nodo_bfs:
        nodo_actual = nodo_bfs
        while nodo_actual.get_padre() is not None:
            resultado_bfs.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        resultado_bfs.append(nodo_actual.get_datos())
        resultado_bfs.reverse()
    resultados['BFS'] = resultado_bfs

    # Resolver usando LIFO (DFS del archivo lifo.py)
    resultado_lifo = []
    nodo_lifo = buscar_solucion_DFS(estado_inicial, solucion)
    if nodo_lifo:
        nodo_actual = nodo_lifo
        while nodo_actual.get_padre() is not None:
            resultado_lifo.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        resultado_lifo.append(nodo_actual.get_datos())
        resultado_lifo.reverse()
    resultados['LIFO'] = resultado_lifo

    # Pasar todos los resultados a la plantilla
    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
