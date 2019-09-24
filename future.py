from concurrent.futures import ThreadPoolExecutor
import time


def how_many_vegetables():
    print('Olivia is counting vegetables...')
    time.sleep(3)
    return 42


if __name__ == '__main__':
    print('Barron ask Olivia how many vegetables in pantry.')
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_many_vegetables)
        print('Barron can do other thing while he is waits for other results')
        print('Olivia responded with', future.result())
