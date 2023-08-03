import multiprocessing
import time
import colorama

def processar(size):
    print(colorama.Fore.WHITE + "[", end="", flush=True)
    
    for _ in range(1,size):
        print(colorama.Fore.GREEN + "X", end="", flush=True)
        time.sleep(0.1)
    
    print(colorama.Fore.WHITE + "]", end="", flush=True)
    print()

if __name__ == "__main__":
    p = multiprocessing.Process(target=processar, args=(10,))
    p.start()
    p.join()


