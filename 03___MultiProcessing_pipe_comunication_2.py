import multiprocessing
import time

def ping(queue):
    queue.put('Gustavo')

def pong(queue):
    msg = queue.get()
    print(f'{msg} Braga')

if __name__ == '__main__':
    
    queue = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
