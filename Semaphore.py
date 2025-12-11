import threading
import time


receptioncet = threading.Semaphore()

def enter_examinationroom(n):
    print(f"patient {n} is wating for is turn")
    receptioncet.acquire()
    print(f"patient {n} is in the examination")
    time.sleep(4)
    print(f"patient {n} is out of thee xamination")
    receptioncet.release()
      
    
    
    
patients = []
for i in range(10):
    patient = threading.Thread(target=enter_examinationroom,args=(i,))
    patients.append(patient)
    patient.start()
