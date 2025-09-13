from multiprocessing import Process, Queue
import time, random

def producer(q, total_items=20):
    for i in range(1, total_items+1):
        time.sleep(random.uniform(0.01, 0.15))  # simula produção
        q.put(i)
        print(f"Produtor produziu {i}")
    q.put(None)  # sentinel para indicar fim

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            # repassa sentinel caso haja mais consumidores (não necessário se só 1)
            print("Consumidor recebeu sentinel e vai terminar.")
            break
        print(f"Consumidor processou {item}")
        time.sleep(random.uniform(0.02, 0.2))  # simula consumo
    print("Consumidor finalizado.")

if __name__ == '__main__':
    q = Queue(maxsize=5)  # buffer limitado
    p = Process(target=producer, args=(q, 30))
    c = Process(target=consumer, args=(q,))
    p.start(); c.start()
    p.join(); c.join()
    print("Producer-Consumer finalizado.")
