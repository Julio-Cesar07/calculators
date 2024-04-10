from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1
from .Mock.flask_request_mock import MockRequest

def test_calculate():
    calculator_1 = Calculator1()
    
    mock_request = MockRequest(body={ "number": 1 })
    
    response = calculator_1.calculate(request=mock_request)
    
    # Formato da response
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    
    # Assertividade da response
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    calculator_1 = Calculator1()
    
    mock_request = MockRequest(body={ "not-exists": 1 })
    
    with raises(Exception) as excinfo:
        calculator_1.calculate(request=mock_request)
    
    # Formato da response
    assert str(excinfo.value) == 'Body mal formatado!'
