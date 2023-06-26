from collections import deque
import time

class ParqueTemático:
    def __init__(self):
        self.fila = deque()

    def entrar_na_fila(self, visitante):
        self.fila.append(visitante)
        print(f"{visitante} entrou na fila.")

    def sair_da_fila(self):
        if self.fila:
            visitante = self.fila.popleft()
            print(f"{visitante} saiu da fila e entrou no parque.")
        else:
            print("A fila está vazia.")

    def exibir_fila(self):
        print("Fila atual:")
        if self.fila:
            for visitante in self.fila:
                print(visitante)
        else:
            print("A fila está vazia.")

    def remover_desistentes(self):
        if self.fila:
            print("Removendo desistentes...")
            if self.fila:
                visitante = self.fila.pop()
                print(f"{visitante} foi removido da fila.")
            if not self.fila:
                print("A fila está vazia após remover desistentes.")
        else:
            print("A fila está vazia.")

if __name__ == "__main__":
    parque = ParqueTemático()
    
    while True:
        print("\n=== Menu ===")
        print("1. Entrar na fila")
        print("2. Sair da fila")
        print("3. Exibir fila")
        print("4. Remover desistentes da fila")
        print("5. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visitante = input("Digite o nome do visitante: ")
            parque.entrar_na_fila(visitante)
        elif opcao == "2":
            parque.sair_da_fila()
        elif opcao == "3":
            parque.exibir_fila()
        elif opcao == "4":
            parque.remover_desistentes()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")