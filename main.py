import venusian
import fixture
from fixture.dec import found
import time
import pkgutil

def scan():
    found[:] = []
    scanner = venusian.Scanner()
    scanner.scan(fixture)

def loadmodules():
    for module_loader, name, ispkg in pkgutil.iter_modules(['fixture']):
        loader = module_loader.find_module(name)
        module = loader.load_module(name)

if __name__ == '__main__':
    start = time.time()
    scan()
    end = time.time()
    print "Time to scan modules with Venusian: ", end - start

    start = time.time()
    loadmodules()
    end = time.time()
    print "Time to import all modules (including Venusian decorators): ", end - start
