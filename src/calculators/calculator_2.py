from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        
        input_data = self.__validate_body(body=body)
        
        first_process = self.__first_process(input_data=input_data)

        response = self.__format_response(calc_result=first_process)

        return response
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or (not isinstance(body['numbers'], List) or not all(isinstance(num, (float, int)) for num in body['numbers'])):
            raise HttpUnprocessableEntityError('Body mal formatado!')

        input_data = body.get('numbers')
        return input_data
    
    def __first_process(self, input_data: List[float]) -> float:
        first_part = [(num * 11) ** 0.95 for num in input_data]

        result = self.__driver_handler.standard_derivation(first_part)

        return 1/result
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }