from multiprocessing import Process, Queue
import time, random

def aluno(name, q):
    for i in range(1, 4):  # 3 mensagens
        msg = f"{name}: mensagem {i}"
        q.put(msg)
        time.sleep(random.uniform(0.05, 0.3))

if __name__ == '__main__':
    q = Queue()
    processos = [Process(target=aluno, args=(f"Aluno{i}", q)) for i in range(1, 4)]

    for p in processos:
        p.start()

    total_msgs = 3 * len(processos)
    for _ in range(total_msgs):
        mensagem = q.get()  # bloqueia até receber
        print("Mensagem recebida ->", mensagem)

    for p in processos:
        p.join()

    print("Chat finalizado.")
