from multiprocessing import Process, Value, Lock
import time

def worker(counter, n, lock=None):
    for _ in range(n):
        if lock:
            # proteção com lock
            with lock:
                counter.value += 1
        else:
            # sem proteção -> condição de corrida
            counter.value += 1

if __name__ == '__main__':
    ITER = 1000

    # --- Sem lock ---
    counter = Value('i', 0)  # inteiro compartilhado
    p1 = Process(target=worker, args=(counter, ITER))
    p2 = Process(target=worker, args=(counter, ITER))
    p1.start(); p2.start()
    p1.join(); p2.join()
    print("Sem lock -> esperado 2000, obtido:", counter.value)

    # --- Com lock ---
    counter = Value('i', 0)
    lock = Lock()
    p1 = Process(target=worker, args=(counter, ITER, lock))
    p2 = Process(target=worker, args=(counter, ITER, lock))
    p1.start(); p2.start()
    p1.join(); p2.join()
    print("Com lock -> esperado 2000, obtido:", counter.value)
