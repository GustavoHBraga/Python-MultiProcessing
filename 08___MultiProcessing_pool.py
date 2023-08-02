import multiprocessing
import time

def calcular(valor):
    return valor ** 2

def current_process_name():
    print(multiprocessing.current_process().name)

def main():
    tamanho_pool = multiprocessing.cpu_count() * 2 # 4 cores * 2 = 8
    
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=current_process_name)
    
    entradas = list(range(11))
    saidas = pool.map(calcular,entradas)

    print(f"Saidas {saidas}")
    
    pool.close()
    pool.join()

def main2():
    entradas = list(range(11))
    saidas = []
    for valor in entradas:
        saidas.append(calcular(valor))
    print(f"Saidas {saidas}")

if __name__ == "__main__":
    main()