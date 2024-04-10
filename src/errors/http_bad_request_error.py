from src.errors.error_handler import ErrorHandler

class HttpBadRequestError(ErrorHandler):
    def __init__(self, message: str) -> None:
        super().__init__(message, 400, "Http Bad Request")