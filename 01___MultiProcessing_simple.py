import multiprocessing
import time

print(f"Iniciando o processo com {multiprocessing.current_process().name} ")

def fazer_qualquer_coisa(valor):
    print(f"Estou fazendo alguma coisa {valor}")
    

def main():
    processo = multiprocessing.Process(target=fazer_qualquer_coisa, args=(1,),name="fazer_qualquer_coisa")
    processo.start()
    processo.join()
    

if __name__ == "__main__":
    main()