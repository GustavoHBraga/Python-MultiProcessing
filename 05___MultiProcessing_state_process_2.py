import multiprocessing
import time
import ctypes 

def funcao1(val,stat):
    
    if stat.value:
        res = val.value + 10
        stat.value = False

    else:
        res = val.value + 20
        val.value = 200
        stat.value = True

    print(f"o resultado da funcao 1 = {res}") # 120
    time.sleep(0.001)

def funcao2(val,stat):
    
    if stat.value:
        res = val.value + 30 # 230
        stat.value = False
        
    else:
        res = val.value + 40
        val.value = 400
        stat.value = True

    print(f"o resultado da funcao 2 = {res}")
    time.sleep(0.001)

def main():
    valores = multiprocessing.Value(ctypes.c_int, 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=funcao1, args=(valores,status))
    p2 = multiprocessing.Process(target=funcao2, args=(valores,status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()