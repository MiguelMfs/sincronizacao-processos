from multiprocessing import Process, Semaphore
import time, random

def aluno(name, sem):
    print(f"{name} quer usar o laboratório.")
    sem.acquire()
    try:
        print(f"{name} entrou no laboratório.")
        time.sleep(random.uniform(0.5, 2.0))  # usando recurso
        print(f"{name} terminou e está saindo.")
    finally:
        sem.release()

if __name__ == '__main__':
    NUM_RECURSOS = 3   # por exemplo, 3 estações no lab
    NUM_ALUNOS = 7
    sem = Semaphore(NUM_RECURSOS)

    procs = [Process(target=aluno, args=(f"Aluno{i}", sem)) for i in range(1, NUM_ALUNOS+1)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print("Todos os alunos passaram pelo laboratório.")
