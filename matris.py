"""
"""

class Ex(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__mes = message
    def __str__(self):
        return f'Error: {self.__mes}'

class Matrix:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check(can):
        """

        """
        # temp = len(can[0])
        # for item in can:
        #     if len(item) != temp:
