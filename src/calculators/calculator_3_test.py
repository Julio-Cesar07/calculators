from pytest import raises
from .Mock.driver_handler_interface import MockDriverHandler
from .Mock.flask_request_mock import MockRequest
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
    
def test_calculate():
    calculator_3 = Calculator3(driver_handler=MockDriverHandler())

    mock_request = MockRequest({ "numbers": [1, 2, 30]})
    
    response = calculator_3.calculate(request=mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "value" in response["data"]
    assert "Success" in response["data"]
    
    # Assertividade da response
    assert isinstance(response["data"]["value"], float)
    assert response["data"]["Calculator"] == 3
    assert response["data"]["Success"] == True
    
def test_calculate_integration():
    calculator_3 = Calculator3(driver_handler=NumpyHandler())

    mock_request = MockRequest({ "numbers": [1, 2, 30]})

    response = calculator_3.calculate(request=mock_request)
    
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "value" in response["data"]
    assert "Success" in response["data"]
    
    # Assertividade da response
    assert isinstance(response["data"]["value"], float)
    assert response["data"]["Calculator"] == 3
    assert response["data"]["Success"] == True

def test_calculate_with_variance_error():
    calculator_3 = Calculator3(driver_handler=NumpyHandler())

    mock_request = MockRequest({ "numbers": [1, 2, 3]})

    with raises(Exception) as execinfo:
        calculator_3.calculate(request=mock_request)

    assert str(execinfo.value) == 'Falha no processo: Variância menor do que multiplicação.'
    
    
    
    