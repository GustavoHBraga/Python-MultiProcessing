import multiprocessing
import time

def funcao1(val,stat):
    
    if stat:
        res = val + 10
        stat = False

    else:
        res = val + 20
        val = 200
        stat = True

    print(f"o resultado da funcao 1 = {res}")
    time.sleep(0.001)

def funcao2(val,stat):
    
    if stat:
        res = val + 30
        stat = False
        
    else:
        res = val + 40
        val = 400
        stat = True

    print(f"o resultado da funcao 2 = {res}")
    time.sleep(0.001)

def main():
    valores = 100
    status = False

    p1 = multiprocessing.Process(target=funcao1, args=(valores,status))
    p2 = multiprocessing.Process(target=funcao2, args=(valores,status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()