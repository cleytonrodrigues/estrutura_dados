import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
        
    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        
        return node
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
        
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
            
        return node
    
    def _get_min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)
            
            
    def get_graph(self, node, graph=None):
        if graph is None:
            graph = nx.DiGraph()
            
        if node:
            graph.add_node(node.value)
            if node.left:
                graph.add_edge(node.value, node.left.value)
                self.get_graph(node.left, graph)
            if node.right:
                graph.add_edge(node.value, node.right.value)
                self.get_graph(node.right, graph)
        
        return graph
    
    def draw_tree(self, graph):
        pos = self.hierarchy_pos(graph, self.root, width=1., vert_gap=0.2, vert_loc=0)
        nx.draw(graph, pos=pos, with_labels=True, node_size=1000, node_color='skyblue')
        
    def hierarchy_pos(self, graph, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        pos = {root.value: (xcenter, vert_loc)}
        neighbors = list(graph.neighbors(root.value))
        if len(neighbors) != 0:
            dx = width / 2
            nextx = xcenter - width/2 - dx/2
            for neighbor in neighbors:
                nextx += dx
                pos[neighbor] = (nextx, vert_loc - vert_gap)
                pos.update(self.hierarchy_pos(graph, Node(neighbor), width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx))
        return pos

# Exemplo de uso
binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(8)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(15)
binary_tree.insert(10)
binary_tree.insert(20)

'''
print("Árvore Binária antes da exclusão:")
binary_tree.inorder_traversal(binary_tree.root)
print()

delete_value = 8
binary_tree.delete(delete_value)

print(f"Árvore Binária após a exclusão do valor {delete_value}:")
binary_tree.inorder_traversal(binary_tree.root)
'''

# Antes da exclusão
plt.figure(figsize=(8, 6))
graph_before = binary_tree.get_graph(binary_tree.root)
binary_tree.draw_tree(graph_before)
plt.title("Árvore Binária Antes da Exclusão")
plt.axis('off')
plt.show()
#pos = nx.spring_layout(graph_before, seed=42)
#nx.draw(graph_before, pos, with_labels=True, node_size=1000, node_color='skyblue')
#plt.title("Árvore Binária Antes da Exclusão")
#plt.show()

delete_value = 5
binary_tree.delete(delete_value)

# Após a exclusão
plt.figure(figsize=(8, 6))
graph_after = binary_tree.get_graph(binary_tree.root)
binary_tree.draw_tree(graph_after)
plt.title("Árvore Binária Após a Exclusão")
plt.axis('off')
plt.show()
#pos = nx.spring_layout(graph_after, seed=42)
#nx.draw(graph_after, pos, with_labels=True, node_size=1000, node_color='lightgreen')
#plt.title(f"Árvore Binária Após a Exclusão do Valor {delete_value}")
#plt.show()