#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

"""
Counts number of pulses for 1 second and prints.
"""

from pydaqmx_helper.counter import Counter
from time import sleep

myCounter = Counter()
myCounter.start()
sleep(1)
counts = myCounter.stop()
print("Counts:",counts) 
