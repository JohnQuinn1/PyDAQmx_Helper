#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

"""
Should produce a histogram plot of counts in given interval(seconds) 
Also saves a python list of the raw and frequency counts data to files. 
"""

from pydaqmx_helper.counter import Counter
from time import sleep
import matplotlib.pyplot as plt
import numpy as np


myCounter = Counter()
data = np.zeros(8)
rawData = []
interval = 0.01

for i in range(0, 1000):
    myCounter.start()
    sleep(interval)
    count = myCounter.stop()
    if i % 100 == 0:
        print(str(i) + ' counts')
    rawData.append(count)
    data[count] = data[count] + 1.0

print("Variance of counts in %d", interval)
print(np.var(rawData))
print("Mean of counts in %d", interval)
print(np.mean(rawData))
print("Frequency counts")
print(data)

print("Saving raw and frequency counts to file")

f = open('rawCounterData.txt', 'w')
f.write(repr(rawData))
f.close()

f = open('frequencyCounterData.txt', 'w')
f.write(repr(data))
f.close()

plt.hist(rawData, bins=6)
plt.show()
