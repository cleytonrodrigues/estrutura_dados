from queue import Queue
import random

def jogo_numero_sorte():
    # Inicializa a fila
    fila = Queue()

    # Gera um número aleatório de 1 a 100
    numero_sorte = random.randint(1, 100)

    # Loop principal do jogo
    while True:
        # Solicita o palpite do jogador
        palpite = int(input("Digite um número entre 1 e 100: "))

        # Verifica se o palpite está correto
        if palpite == numero_sorte:
            print("Parabéns! Você acertou o número da sorte!")
            break
        else:
            # Adiciona o palpite à fila
            fila.put(palpite)
            print("Palpite errado! Continue tentando.")

        # Verifica se há jogadores suficientes para exibir uma dica
        if fila.qsize() >= 3:
            dica = random.choice(list(fila.queue))
            print("Dica: Um dos jogadores anteriores tentou o número", dica)

    print("Fim do jogo.")

def main():
    # Inicia o jogo
    jogo_numero_sorte()

if __name__ == "__main__":
    main()