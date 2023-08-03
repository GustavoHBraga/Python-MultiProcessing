#from concurrent.futures.process import ProcessPoolExecutor as Executor 
from concurrent.futures.thread import ThreadPoolExecutor as Executor
import time

def processar():
    print("[", end="", flush=True)
    
    for _ in range(1,10):
        print("X", end="", flush=True)
        time.sleep(0.3)
    
    print("]", end="", flush=True)
    print()

if __name__ == "__main__":
    with Executor(max_workers=3) as executor:
        future = executor.submit(processar)


