from py_futbol.adapters.driven.test.test import Test
from py_futbol.app.sclubman.sclubman_fin import SclubmanFin

def run_basic_configurator():
    # initialize driven adapters

    # initialize app ports
    fin = SclubmanFin()

    # initialize driving adapters
    # test.py
    test = Test(fin)

    # run program
    test.run()