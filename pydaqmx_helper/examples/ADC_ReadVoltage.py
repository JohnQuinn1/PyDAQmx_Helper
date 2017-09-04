from __future__ import print_function
"""
Example program to show how to read from a single ADC channel with default settings
Should print out the correct voltage value for channel 0
"""

from pydaqmx_helper.adc import ADC

myADC = ADC()
myADC.addChannels([0])
val = myADC.readVoltage()
print(val)

