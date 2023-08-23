class Grafo:
    def __init__(self, vertices, matriz_adjacencia):
        self.vertices = vertices
        self.matriz_adjacencia = matriz_adjacencia
    
    def obter_vertices(self):
        return self.vertices
    
    def obter_arestas(self):
        arestas = []
        for i in range(len(self.matriz_adjacencia)):
            for j in range(len(self.matriz_adjacencia[i])):
                if self.matriz_adjacencia[i][j] != 0:
                    arestas.append((self.vertices[i], self.vertices[j], self.matriz_adjacencia[i][j]))
        return arestas

vertices = ['A', 'B', 'C']
matriz_adjacencia = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

g = Grafo(vertices, matriz_adjacencia)

print("Vértices:", g.obter_vertices())
print("Arestas:", g.obter_arestas())