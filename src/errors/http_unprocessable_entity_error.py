from src.errors.error_handler import ErrorHandler

class HttpUnprocessableEntityError(ErrorHandler):
    def __init__(self, message: str) -> None:
        super().__init__(message, 422, "Http Unprocessable Entity")