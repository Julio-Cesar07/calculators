from typing import Dict
from .error_handler import ErrorHandler

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, ErrorHandler):
        return {
            "status_code": error.get_statusCode(),
            "body": {
                "erros": [{
                    "title": error.get_name(),
                    "detail": error.get_message()
                }]
                },
        }
    
    return {
        "status_code": 500,
        "body": {
                "erros": [{
                    "title": "Server Error",
                    "detail": str(error)
                }]
                },
    }