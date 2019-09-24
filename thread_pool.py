import threading


def vegetable_chopper(vegetable_id):
    name = threading.current_thread().getName()
    print(name, 'chopper vegetable', vegetable_id)


if __name__ == '__main__':
    for vegetable in range(100):
        threading.Thread(target=vegetable_chopper, args=(vegetable,)).start()
