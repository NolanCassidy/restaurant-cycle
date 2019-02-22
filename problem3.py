import sys
from queue import Queue
from collections import *

def driver():
    q1 = Queue()
    q2 = Queue()
    start = 0
    count = 0
    f = open(sys.argv[1])
    lines = int(f.readline().strip())
    for line in f:
            line = line.strip().split()
            c = int(line[0])-int(line[1])
            q1.enqueue(c)
            count += c
            while count < 0:
                d = q1.dequeue()
                count -= d
                q2.enqueue(d)
                start+=1
    print(start)


if __name__ == "__main__":
    driver()
