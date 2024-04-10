from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3.14
    
    def variance(self, numbers: List[float]) -> float:
        return 300.1415