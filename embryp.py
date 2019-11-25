import multiprocessing
import time


def worker(interval):
    energy = 1000
    while True:
        print("The time is {0}".format(time.ctime()))  # 输出时间的格式
        time.sleep(interval)
        energy -= 1


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,))
    p.start()
    print("p.pid:", p.pid)
    print("p.name:", p.name)
    print("p.is_alive:", p.is_alive())
