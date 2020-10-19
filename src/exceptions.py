class WrongSubError(Exception):
    mes = "WRONG SUB FOO"
    def __init__(self, message=mes):
        super().__init__(message)

class NotSortedError(Exception):
    message = "List was not sorted properly"
    def __init__(self, message=message):
        super().__init__(message)

