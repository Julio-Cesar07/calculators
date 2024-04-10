from typing import Dict
from flask import Request as FlaskRequest
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate__body(body)
        
        splitted_number = input_data / 3
        
        first_process_result = self.__first_process(first_number=splitted_number)
        second_process_result = self.__second_process(second_number=splitted_number)
        third_process_result = self.__third_process(third_number=splitted_number)
        
        calc_result = first_process_result + second_process_result + third_process_result

        response = self.__format_response(calc_result=calc_result)
        return response
        
    def __validate__body(self, body: Dict) -> float:
        if "number" not in body or (not isinstance(body['number'], float) and not isinstance(body['number'], int)):
            raise HttpUnprocessableEntityError('Body mal formatado!')
        
        input_data = body.get('number')
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part
    
    def __third_process(self, third_number: float) -> float:
        return third_number
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }