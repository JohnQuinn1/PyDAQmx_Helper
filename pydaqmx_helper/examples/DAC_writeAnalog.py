#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Example program to show how to write a single
2.62v voltage to the first DAC channel. """

from pydaqmx_helper.dac import DAC
myDAC = DAC(0)
myDAC.writeVoltage(2.62)
