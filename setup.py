"""
This is a setup.py script generated by py2applet to execute this code and create the macOS standalone application. 

* Usage:
Write the following line of code in your terminal.

    python3 setup.py py2app
    
"""


from setuptools import setup
import glob 

APP = ['GUI.py']
DATA = [('avgWaveData8by8', glob.glob('./numpyArrays8by8/*.npy')),('GUI_images', glob.glob('./GUI_images/logo.png'))]
OPTIONS = {'iconfile': './GUI_images/application.icns'}

setup(
    app=APP,
    data_files=DATA,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name ='Spatial labelling',
    version='1.2'
)

