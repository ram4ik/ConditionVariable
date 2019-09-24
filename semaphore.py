import random
import threading
import time

charger = threading.Semaphore(4)


def cellphone():
    name = threading.current_thread().getName()
    charger.acquire()
    print(name, 'is charging...')
    time.sleep(random.uniform(1,2))
    print(name, 'is DONE charging!')
    charger.release()


if __name__ == '__main__':
    for phone in range(2):
        threading.Thread(target=cellphone, name='Phone'+str(phone)).start()