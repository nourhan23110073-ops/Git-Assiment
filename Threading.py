import threading
import time



def print_1():
    print("start of the thread",threading.current_thread().name)
    time.sleep(2)
    print("finshid of the thread",threading.current_thread().name)
    
      
def print_2():
    print("start of the thread",threading.current_thread().name)
    print("finshed of the thread",threading.current_thread().name)
    
    
a = threading.Thread(target=print_1,name="thread1")      
b = threading.Thread(target=print_2,name="thread2")  

a.start()
b.start()    
