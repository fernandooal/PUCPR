import threading
import time
import random

N = 5 

# semáforos
garfos = [threading.Semaphore(1) for _ in range(N)]

# semáforo para evitar deadlock - garantir que no máximo N-1 filósofos tentem pegar garfos
controle = threading.Semaphore(N - 1)

mutex = threading.Semaphore(1) 

def filosofo(id):
    while True:
        with mutex:
            print(f"Filósofo {id} está pensando")
        time.sleep(random.uniform(1, 3))
        
        with controle:
            garfo_direito = id
            # % N que o filósofo 4 pegue o garfo 0 na esquerda
            garfo_esquerdo = (id + 1) % N
            
            garfos[garfo_direito].acquire()
            with mutex:
                print(f"Filósofo {id} pegou garfo {garfo_direito} (direito)")
            
            time.sleep(random.uniform(0.1, 0.5))
            
            garfos[garfo_esquerdo].acquire()
            with mutex:
                print(f"Filósofo {id} pegou garfo {garfo_esquerdo} (esquerdo)")
                print(f"Filósofo {id} está comendo")
        
        time.sleep(random.uniform(1, 2))
        
        garfos[garfo_esquerdo].release()
        garfos[garfo_direito].release()
        with mutex:
            print(f"Filósofo {id} liberou garfos {garfo_esquerdo} (esquerdo) e {garfo_direito} (direito)")

filosofos = [
    threading.Thread(target=filosofo, args=(0,), name="Filósofo 0", daemon=True),
    threading.Thread(target=filosofo, args=(1,), name="Filósofo 1", daemon=True),
    threading.Thread(target=filosofo, args=(2,), name="Filósofo 2", daemon=True),
    threading.Thread(target=filosofo, args=(3,), name="Filósofo 3", daemon=True),
    threading.Thread(target=filosofo, args=(4,), name="Filósofo 4", daemon=True)
]

[f.start() for f in filosofos]

time.sleep(30)
print("FIM")