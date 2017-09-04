#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Example program to show how to read multiple
samples from a single ADC channel with a
user-specified range at a given sample rate
Should print out 50 samples
"""

from pydaqmx_helper.adc import ADC

myADC = ADC()
myADC.addChannels([0], ADC_mode='DAQmx_Val_Diff', minRange=-5.0,
                   maxRange=5.0)

# Returns a dictionary with voltages and channels as key value pairs.
# Here we get the values from channel 0

samples = myADC.sampleVoltages(50, 10)[0]
for sample in samples:
    print(sample)
