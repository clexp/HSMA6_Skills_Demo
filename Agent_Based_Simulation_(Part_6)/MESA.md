# MESA

MESA is an oss for agent based simulation in python
it is modular.  
It has modules for visualizing, analysis and modelling

You need one (probably two) python files. One for the model, and one for the server visualising the model

The output from this is pretty rubbish. You get a grid of coloured dots that change forth and back.

This is much more difficult to use than it needs to be. Issues:

1. It rejects web page requests, if the referrer is not specified (all except firefox)
2. You have to run it from the command line, running it from vscode gives you 'mesa not installed' even though it is, and can confirm this in the conda venv.
3. If it returns a page, it is just the text of the code, not a graphical front end. There is not a way to run this from the jupyter window
4. Some blogs have a run.py file, some don't
5. The docs indicate you run it from python or from jupyter, but not sure which
6. The HSMA6 lecture notes is somewhat bereft of the functional server.py file
7. The HSMA old worked examples do not use any of the modern visualisation, nor have a run.py file
