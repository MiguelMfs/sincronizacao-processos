from multiprocessing import Process, Queue
import time, random

def player(pid, my_q, next_q):
    while True:
        token = my_q.get()
        if token is None:
            # propaga sinal de término para o próximo e sai
            next_q.put(None)
            print(f"Player {pid} recebeu sinal de término e encerra.")
            break

        # token é um dict contendo 'passes' restante
        token['passes'] -= 1
        print(f"Player {pid} pegou a batata (passes restantes: {token['passes']})")
        time.sleep(random.uniform(0.05, 0.3))

        if token['passes'] <= 0:
            # fim do jogo: envia sentinel para parar a cadeia
            print(f"Player {pid} terminou o jogo (batata final).")
            next_q.put(None)
            break
        else:
            # passa adiante
            next_q.put(token)

if __name__ == '__main__':
    NUM_PLAYERS = 5
    TOTAL_PASSES = 12  # número total de passadas antes de encerrar

    # cria uma fila por jogador (anel)
    queues = [Queue() for _ in range(NUM_PLAYERS)]
    procs = []
    for i in range(NUM_PLAYERS):
        p = Process(target=player, args=(i, queues[i], queues[(i+1) % NUM_PLAYERS]))
        procs.append(p)

    for p in procs:
        p.start()

    # inicia o token no jogador 0
    token = {'passes': TOTAL_PASSES}
    queues[0].put(token)

    for p in procs:
        p.join()

    print("Jogo da batata quente finalizado.")
