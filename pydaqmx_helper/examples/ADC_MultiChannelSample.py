#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Example program to show how to read multiple
samples from multiple ADC channels at a given sample rate
"""

from pydaqmx_helper.adc import ADC

myADC = ADC()
myADC.addChannels([0, 1, 2])
samples = myADC.sampleVoltages(10, 10)

print("Samples for Channel 0:",samples[0])
print("Samples for Channel 1:",samples[1])
print("Samples for Channel 2:",samples[2])
