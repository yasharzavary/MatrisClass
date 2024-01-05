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
        self.__data = data if self.check(data) else self.__valid1D(data)

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

        for item in can:
            if not isinstance(item,  list): return False
        temp = len(can[0])
        for item in can:
            if len(item) != temp:
                if t == 'b' : return False
                raise Ex('this input isn\'t matrix type...please check it')
        return True

    def __valid1D(self, canData):
        for item in canData:
            if isinstance(item, tuple) or isinstance(item, set): raise TypeError('please use list in matrix')
            if isinstance(item, list): raise TypeError('invalid matrix, please check rows and columns')
        return [canData]

    def connect(self, other):
        pass

    def determineRC(self):
        pass

    def __str__(self):
        return str(self.__data)
    


