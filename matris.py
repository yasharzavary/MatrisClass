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

    def __getitem__(self, index):
        temp = self.__data
        if isinstance(index, slice):
            return Matrix(temp[index.start:index.stop:index.step]) if len(temp) != 1 else temp[0][index.start:index.stop:index.step]
        try:
            return Matrix(temp[index]) if len(temp) != 1 else temp[0][index]
        except:
            raise IndexError('check your index for matrix')

    @property
    def mData(self):
        return self.__data

    @mData.setter    
    def mData(self, newData):
        self.__data = self.check(newData)

    @property
    def size(self):
        if self.isEmpty: return 0,0
        return len(self.__data), len(self.__data[0])

    @property
    def isEmpty(self):
        if not self.__data:
            return True
        return False

    def squareChecker(self):
        temp = self.size
        return True if temp[0] == temp[1] else False

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
        # for type similarity checking
        rule = type(canData[0])
        for item in canData:
            if isinstance(item, tuple) or isinstance(item, set): raise TypeError('please use just list in matrix')
            if type(item) != rule: raise TypeError('please recheck the matrix ingridents')

        return [canData] if not isinstance(canData[0], list) else canData

    def connect(self, other, t = True):
        # TODO: correct empty list connection 
        # TODO: from row or col connect op
        # TODO: both of them empty
        """
        it will connect two matrix with togheter and send it back
        other: second matrix or list for connecting
        t: you can set it to False to return list 
        return: one matrix(in list type)
        """
        if isinstance(other, Matrix) :
            if other.isEmpty:
                return self if t else self.__data
            elif self.isEmpty:
                return other if t else other.mData
            return self.__data + other.mData if not t else Matrix(self.__data + other.mData)
        if not isinstance(other, list): raise TypeError('please check second matrix')
        if self.isEmpty:
            return Matrix(other) if t else other
        elif len(other) == 0:
            return self if t else self.__data
        return self.__data + self.__valid1D(other) if not t else Matrix(self.__data + self.__valid1D(other))

    def determineRC(self):
        pass

    def __str__(self):
        return str(self.__data)
    


