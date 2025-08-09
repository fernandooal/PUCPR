import multiprocessing
import time

# versão básica (com condição de corrida)
def incrementar_estoque_basic(estoque):
    estoque = estoque + 1
    print(f'Estoque do processo {multiprocessing.current_process().name}: {estoque}')
    time.sleep(0.001)

# versão correta com Value e Lock
def incrementar_estoque_lock(estoque):
    with estoque.get_lock():
        estoque.value += 1
        print(f'Estoque do processo {multiprocessing.current_process().name}: {estoque.value}')
    time.sleep(0.001)

# versão com Queue
def incrementar_estoque_queue(q):
    estoque = q.get()
    estoque += 1
    print(f'Estoque do processo {multiprocessing.current_process().name}: {estoque}')
    q.put(estoque)
    time.sleep(0.001)

# versão com Pipe
def incrementar_estoque_pipe(conn):
    estoque = conn.recv()
    estoque += 1
    print(f'Estoque do processo {multiprocessing.current_process().name}: {estoque}')
    conn.send(estoque)
    time.sleep(0.001)

def main():
    # teste versão básica
    print("=== Versão Básica (com condição de corrida) ===")
    estoque = 0
    
    start_time = time.time()
    m1 = multiprocessing.Process(target=incrementar_estoque_basic, args=(estoque,), name="Máquina 1")
    m2 = multiprocessing.Process(target=incrementar_estoque_basic, args=(estoque,), name="Máquina 2")
    m3 = multiprocessing.Process(target=incrementar_estoque_basic, args=(estoque,), name="Máquina 3")

    m1.start()
    m2.start()
    m3.start()
    
    m1.join()
    m2.join()
    m3.join()
    
    end_time = time.time()
    print(f'Tempo: {end_time-start_time:.4f} segundos')
    print('-------')

    # teste versão com Value e Lock
    print("=== Versão com Value e Lock ===")
    estoque = multiprocessing.Value('i', 0)
    
    start_time = time.time()
    m1 = multiprocessing.Process(target=incrementar_estoque_lock, args=(estoque,), name="Máquina 1")
    m2 = multiprocessing.Process(target=incrementar_estoque_lock, args=(estoque,), name="Máquina 2")
    m3 = multiprocessing.Process(target=incrementar_estoque_lock, args=(estoque,), name="Máquina 3")

    m1.start()
    m2.start()
    m3.start()
    
    m1.join()
    m2.join()
    m3.join()
    
    end_time = time.time()
    print(f'Tempo: {end_time-start_time:.4f} segundos')
    print(f'Estoque final: {estoque.value}')
    print('-------')

    # teste versão com Queue
    print("=== Versão com Queue ===")
    q = multiprocessing.Queue()
    q.put(0)  # valor inicial
    
    start_time = time.time()
    m1 = multiprocessing.Process(target=incrementar_estoque_queue, args=(q,), name="Máquina 1")
    m2 = multiprocessing.Process(target=incrementar_estoque_queue, args=(q,), name="Máquina 2")
    m3 = multiprocessing.Process(target=incrementar_estoque_queue, args=(q,), name="Máquina 3")

    m1.start()
    m2.start()
    m3.start()
    
    m1.join()
    m2.join()
    m3.join()
    
    end_time = time.time()
    print(f'Tempo: {end_time-start_time:.4f} segundos')
    print(f'Estoque final: {q.get() if not q.empty() else "N/A"}')
    print('-------')

    # teste versão com Pipe 
    print("=== Versão com Pipe ===")
    parent_conn, child_conn = multiprocessing.Pipe()
    estoque = 0
    
    start_time = time.time()
    
    parent_conn.send(estoque)
    
    m1 = multiprocessing.Process(target=incrementar_estoque_pipe, args=(child_conn,), name="Máquina 1")
    m2 = multiprocessing.Process(target=incrementar_estoque_pipe, args=(child_conn,), name="Máquina 2")
    m3 = multiprocessing.Process(target=incrementar_estoque_pipe, args=(child_conn,), name="Máquina 3")

    m1.start()
    estoque = parent_conn.recv()
    parent_conn.send(estoque)
    
    m2.start()
    estoque = parent_conn.recv()
    parent_conn.send(estoque)
    
    m3.start()
    estoque = parent_conn.recv()
    
    m1.join()
    m2.join()
    m3.join()
    
    end_time = time.time()
    print(f'Tempo: {end_time-start_time:.4f} segundos')
    print(f'Estoque final: {estoque}')
    print('-------')

if __name__ == '__main__':
    main()