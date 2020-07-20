import random as r
import time
import os

line = []
symbols = ["0", "1"]

for i in range(100):
    x = r.randint(0, 117)
    for i in range(0, x):
        line.append(" ")
    line.append(symbols[r.randint(0, 1)])
    for i in range(10):
        print(*line)
        os.linesep
        time.sleep(0.2)
    line.pop(x)
