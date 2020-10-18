class WrongSubError(Exception):
    mes = "WRONG SUB FOO"
    def __init__(self, message=mes):
        super().__init__(message)