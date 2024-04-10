from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2
from .Mock.flask_request_mock import MockRequest
from .Mock.driver_handler_interface import MockDriverHandler
from src.drivers.numpy_handler import NumpyHandler


# Integração entre Numpy e Calculator2
def test_calculate_integration():
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    
    mock_request = MockRequest(body={ "numbers": [2, 4.657]})

    response = calculator_2.calculate(request=mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    
    # Assertividade da response
    assert isinstance(response["data"]["result"], float)
    assert response["data"]["Calculator"] == 2

def test_calculate():
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    
    mock_request = MockRequest(body={ "numbers": [2, 4.657]})

    response = calculator_2.calculate(request=mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    
    # Assertividade da response
    assert isinstance(response["data"]["result"], float)
    assert response["data"]["Calculator"] == 2
    
def test_calculate_with_body_error():
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver_handler=driver)
    
    mock_request = MockRequest(body={ "numbers": ['1', 'abc'] })
    
    with raises(Exception) as excinfo:
        calculator_2.calculate(request=mock_request)
    
    # Formato da response
    assert str(excinfo.value) == 'Body mal formatado!'