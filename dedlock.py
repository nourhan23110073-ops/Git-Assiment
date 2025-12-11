import threading
import time 

resource_a = threading.Lock()
resource_b = threading.Lock()

def thread_funcution_1():
    with resource_a:
        print("thread1 acqaire resource A")
        time.sleep(2)
        print("thread1 waiting resource B")
        
        with resource_b:
          print("thread1 waiting resource B")   

def thread_funcution_2():
    with resource_b:
        print("thread1 acqaire resource B")
        time.sleep(2)
        print("thread1 waiting resource A")
        
        with resource_a:
          print("thread1 waiting resource A") 
         
            
         
thread1 = threading.Thread(target=thread_funcution_1)
thread2 = threading.Thread(target=thread_funcution_2)
thread1.start()
thread2.start()
