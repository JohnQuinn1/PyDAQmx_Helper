===========
PyDAQmx_Helper
===========

PyDAQmx-Helper provides a set of simplified classes for communicating with the National Instruments USB 6008 module, 
via the PyDAQmx module (which must be installed). They should also work with the USB 6009 although some features 
might be missing. They have been tested and work with Python 3.5. (PyDAQmx? DAQmx?)

The classes provide interfaces for the Analogue-to-Digital (ADC) Convertors, Digital-to-Analogue (DAC) Convertors, 
DigitalIO and Counters.  They were developed for Physics undergraduate laboratories at University College Dublin 
based on in-house C++ classes. These python classes were originally developed by Marco Forte as part of a summer 
internship.

Typical usage often looks like this::

    #!/usr/bin/env python

    from pydaqmx_helper.adc import ADC
    myADC = ADC()
    myADC.addChannels([0])
    val = myADC.readVoltage()
    print(val)


Installation & Upgrade
======================

Download zip and cd to PyDAQmx_Helper folder.

To install: pip install .

To upgrade: pip install —upgrade .


