class Node:
    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, matricula, nome, notas):
        new_node = Node(matricula, nome, notas)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.head is not None:
            current = self.head
            while True:
                print("Matrícula:", current.matricula)
                print("Nome:", current.nome)
                print("Notas:", current.notas)
                print()
                current = current.next
                if current == self.head:
                    break
                
def start():
    # Create a circular linked list
    cll = CircularLinkedList()

    # Append nodes to the list
    cll.append(1, "John Doe", [90, 95, 88])
    cll.append(2, "Jane Smith", [85, 92, 78])
    cll.append(3, "Bob Johnson", [79, 86, 94])

    # Display the contents of the list
    cll.display()

# Run the main function
if __name__ == '__main__':
    start()