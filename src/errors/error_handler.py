from abc import ABC

class ErrorHandler(ABC, Exception):
    def __init__(self, message: str, statusCode: int, name: str) -> None:
        super().__init__(message)
        self.__message = message
        self.__statusCode = statusCode
        self.__name = name

    def get_message(self):
        return self.__message

    def get_statusCode(self):
        return self.__statusCode
    
    def get_name(self):
        return self.__name