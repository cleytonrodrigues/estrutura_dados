class Node:
    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

            
    def append_reverso(self, matricula, nome, notas):
        new_node = Node(matricula, nome, notas)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # Aponta o próximo nó para a antiga cabeça da lista
            self.head = new_node  # Define o novo nó como a nova cabeça da lista

    def display(self):
        current = self.head
        while current is not None:
            print("Matrícula:", current.matricula)
            print("Nome:", current.nome)
            print("Notas:", current.notas)
            print()
            current = current.next
            
            
def start():
    # Criar uma lista encadeada
    lista = LinkedList()

    # Adicionar elementos à lista
    lista.append_reverso(1, "Alice", [8.5, 7.0, 9.0])
    lista.append_reverso(2, "Bob", [6.0, 7.5, 8.0])
    lista.append_reverso(3, "Carol", [9.5, 9.0, 9.5])

    # Exibir os elementos da lista
    lista.display()

if __name__ == "__main__":
    start()