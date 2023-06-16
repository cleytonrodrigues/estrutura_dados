class Node:
    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, matricula, nome, notas):
        new_node = Node(matricula, nome, notas)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current is not None:
            print("Matrícula:", current.matricula)
            print("Nome:", current.nome)
            print("Notas:", current.notas)
            print()
            current = current.next
            
def start():
    # Create a doubly  linked list
    cll = DoublyLinkedList()

    # Append nodes to the list
    cll.append(1, "John Doe", [90, 95, 88])
    cll.append(2, "Jane Smith", [85, 92, 78])
    cll.append(3, "Bob Johnson", [79, 86, 94])

    # Display the contents of the list
    cll.display()

# Run the main function
if __name__ == '__main__':
    start()