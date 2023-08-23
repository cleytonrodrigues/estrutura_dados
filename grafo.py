import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.visitado = False

class Aresta:
    def __init__(self, vertice_origem, vertice_destino, peso):
        self.vertice_origem = vertice_origem
        self.vertice_destino = vertice_destino
        self.peso = peso

class Grafo:
    def __init__(self):
        self.grafo = {}  # Dicionário para armazenar o grafo
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def adicionar_aresta(self, aresta):
        if aresta.vertice_origem in self.grafo and aresta.vertice_destino in self.grafo:
            self.grafo[aresta.vertice_origem].append(aresta)
        else:
            print("Um ou ambos os vértices da aresta não existem no grafo.")
    
    def obter_arestas_adjacentes(self, vertice):
        if vertice in self.grafo:
            return self.grafo[vertice]
        else:
            print("O vértice não existe no grafo.")
            return []
    
    def mostrar(self):
        for vertice in self.grafo:
            arestas_str = [(aresta.vertice_origem.valor, aresta.vertice_destino.valor, aresta.peso) 
                           for aresta in self.grafo[vertice]]
            print(vertice.valor, "->", arestas_str)

# Criar um grafo e adicionar vértices e arestas
g = Grafo()

vertice_a = Vertice('A')
vertice_b = Vertice('B')
vertice_c = Vertice('C')

g.adicionar_vertice(vertice_a)
g.adicionar_vertice(vertice_b)
g.adicionar_vertice(vertice_c)

aresta_ab = Aresta(vertice_a, vertice_b, 3)
aresta_bc = Aresta(vertice_b, vertice_c, 5)
aresta_ca = Aresta(vertice_c, vertice_a, 2)

g.adicionar_aresta(aresta_ab)
g.adicionar_aresta(aresta_bc)
g.adicionar_aresta(aresta_ca)

# Criar um gráfico com networkx e matplotlib
G = nx.DiGraph()

for vertice, arestas in g.grafo.items():
    G.add_node(vertice.valor)
    for aresta in arestas:
        G.add_edge(aresta.vertice_origem.valor, aresta.vertice_destino.valor, weight=aresta.peso)

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()