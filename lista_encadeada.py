class Node:
    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, matricula, nome, notas):
        new_node = Node(matricula, nome, notas)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    def append_index(self, matricula, nome, notas, index):
        new_node = Node(matricula, nome, notas)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current.next is not None:
                    current = current.next
                else:
                    break
            new_node.next = current.next
            current.next = new_node
            
    def remove_index(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next  
                print("oi")
        else:
            current = self.head
            for _ in range(index - 1):
                if current is not None:
                    current = current.next
                else:
                    break
            if current is not None and current.next is not None:
                current.next = current.next.next


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
    lista.append(1, "Alice", [8.5, 7.0, 9.0])
    lista.append(2, "Bob", [6.0, 7.5, 8.0])
    lista.append(3, "Carol", [9.5, 9.0, 9.5])

    # Exibir os elementos da lista
    lista.display()
    
    lista.remove_index(1)
    
    lista.display()

if __name__ == "__main__":
    start()