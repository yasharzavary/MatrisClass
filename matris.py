"""
created by: yashar zavary rezaie


thanks from my dear porfessor Dr.ashrafi
and TA, Eng.sabour
"""

class Ex(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__mes = message
    def __str__(self):
        return f'Error: {self.__mes}'

class Matrix:
    def __init__(self, data) -> None:
        self.__data = self.check(data)

    @property
    def mData(self):
        return self.__data

    @mData.setter    
    def mData(self, newData):
        self.__data = self.check(newData)

    @staticmethod
    def check(can, t='e'):
        # TODO: write document for this function
        """
        :t -> ...
        """
        temp = len(can[0])
        for item in can:
            if len(item) != temp:
                if t == 'b' : return False
                raise Ex('this input isn\'t matrix type...please check it')
        if t == 'b': return True
        return can

    def connect(self):
        pass

    def determineRC(self):
        pass
    


