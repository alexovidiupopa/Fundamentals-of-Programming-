from tests import runTests
from ui import console

def run():
    '''
    The main program, where we only call the tests function and the console one, also initializing the phones list.
    '''
    phones = []
    runTests(phones)
    console(phones)
    
run()