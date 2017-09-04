#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Example program to show how to read multiple
samples from multiple ADC channels at a given sample rate
"""

from pydaqmx_helper.adc import ADC

myADC = ADC()
myADC.addChannels([0, 1, 2])
sample = myADC.sampleVoltages(10, 10)
print(sample)
print('Printing just values ')
print(list(sample.values()))
