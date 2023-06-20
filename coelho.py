import threading
import time
import random

class Coelho(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        distancia = 0
        while distancia < 100:
            # Simula o movimento do coelho
            salto = random.randint(1, 10)
            distancia += salto
            print(f"{self.nome} avançou {salto} unidades. Distância total: {distancia}")
            time.sleep(0.5)  # Espera um curto período de tempo antes do próximo salto

        print(f"{self.nome} terminou a corrida!")

def main():
    # Criação dos coelhos
    coelho1 = Coelho("Coelho 1")
    coelho2 = Coelho("Coelho 2")
    coelho3 = Coelho("Coelho 3")

    # Início da corrida
    coelho1.start()
    coelho2.start()
    coelho3.start()

    # Aguarda todos os coelhos terminarem a corrida
    coelho1.join()
    coelho2.join()
    coelho3.join()

    print("Todos os coelhos terminaram a corrida!")

if __name__ == "__main__":
    main()