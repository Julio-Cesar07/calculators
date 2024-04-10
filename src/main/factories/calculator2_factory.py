from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory() -> Calculator2: 
    numpy_handler = NumpyHandler()
    calc = Calculator2(driver_handler=numpy_handler)
    return calc