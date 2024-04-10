from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.errors.http_bad_request_error import HttpBadRequestError

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        
        input_data = self.__validate_body(body=body)
        
        variance = self.__calculate_variance(numbers=input_data)
        multiplication = self.__calculate_multiplication(numbers=input_data)

        self.__verify_results(multiplication=multiplication, variance=variance)

        response = self.__format_response(variance=variance)

        return response
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or (not isinstance(body['numbers'], List) or not all(isinstance(num, (float, int)) for num in body['numbers'])):
            raise HttpUnprocessableEntityError('Body mal formatado!')

        input_data = body.get('numbers')
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)

        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        
        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError('Falha no processo: Variância menor do que multiplicação.')

        return
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True
            }
        }