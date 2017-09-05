try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='PyDAQmx_Helper',
    version='0.3.0',
    author='Marco Forte',
    author_email='fortemarco.irl@gmail.com',
    maintainer='John Quinn',
    maintainer_email='john.quinn@ucd.ie',
    packages=['pydaqmx_helper', 'pydaqmx_helper.test'],
    license='LICENSE.txt',
    description='Python classes to help with everyday PyDAQmx tasks',
    long_description=open('README.txt').read(),
)
