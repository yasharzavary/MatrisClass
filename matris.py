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
        self.__data = self.check(self.__valid1D(data))

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
        if t not in 'eb': raise Ex('invalid input for return type')
        temp = len(can[0])
        for item in can:
            if len(item) != temp:
                if t == 'b' : return False
                raise Ex('this input isn\'t matrix type...please check it')
        return True if t == 'b' else can

    def __valid1D(self, canData):
        # TODO: write document 
        """
        """
        if not canData: return [[]]
        rule = type(canData[0])
        for item in canData:
            if isinstance(item, tuple) or isinstance(item, set): raise TypeError('please use just list in matrix')
            if type(item) != rule: raise TypeError('please recheck the matrix ingridents')

        return [canData] if not isinstance(canData[0], list) else canData

    def connect(self, other, t = True):
        """
        it will connect two matrix with togheter and send it back
        other: second matrix or list for connecting
        t: you can set it to False to return list 
        return: one matrix(in list type)
        """
        if isinstance(other, Matrix) : return self.__data + other.mData if not t else Matrix(self.__data + other.mData)
        if not isinstance(other, list): raise TypeError('please check second matrix')
        return self.__data + self.__valid1D(other) if not t else Matrix(self.__data + self.__valid1D(other))

    def determineRC(self):
        pass

    def __str__(self):
        return str(self.__data)
    


