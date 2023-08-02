import multiprocessing
import time

def ping(conn):
    conn.send('Gustavo')

def pong(conn):
    msg = conn.recv()
    print(f'{msg} Braga')

if __name__ == '__main__':
    
    conn1, conn2 = multiprocessing.Pipe(True) # Duplex = Ambos se comunicam (Enviar e receber)
    
    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
