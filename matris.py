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
        self.__data = self.check(self.__valid1D(data)) if isinstance(data, list) else self.check(self.__valid1D(Matrix.readFile(data)))

    @staticmethod
    def readFile(p):
        from os import path
        if not path.isfile(p): raise FileNotFoundError('this isn\'t valid path for file')
        with open(p) as file:
            final = []
            for line in file.readlines():
                final.append([float(item) for item in list(line.split())])
        print(final)
        return final


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
        hnList = False
        for item in canData:
            if isinstance(item, tuple) or isinstance(item, set): raise TypeError('please use just list in matrix')
            if not isinstance(item, list): hnList=True
            if isinstance(item, list) and hnList: raise TypeError('please recheck the matrix ingridents')
        return [canData] if not isinstance(canData[0], list) else canData

    @staticmethod
    def filter(d, r, c):
        if isinstance(d, Matrix):
            temp = d.mData
        elif isinstance(d, list):
            temp = d
        returnResult = []
        for row in range(len(temp)):
            if row == r: continue
            returnResult += [temp[row][:c] + temp[row][1+c:]]
        return Matrix(returnResult)

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
        # TODO: adding optinal row and col part
        """

        :return:
        """
        sizeTemp = self.size
        if self.isEmpty: raise Ex('your matrix is empty')
        if sizeTemp == (1, 1): return self[0]
        if sizeTemp == (2, 2): return (self[0][0] * self[1][1]) - (self[1][0] * self[0][1])
        return self.determineG()
        result = 0
        for j in range(sizeTemp[0]):
            chrTemp = self[0][j]
            if chrTemp == 0: continue
            if j % 2 == 0:
                result += chrTemp * Matrix.filter(self.__data, 0, j).determineRC()
            else:
                result -= chrTemp * Matrix.filter(self.__data, 0, j).determineRC()
        return result

    def determineG(self):
        """

        :return:
        """
        detMul = 1
        mTemp = self.__data.copy()
        sizeTemp = self.size
        if self.isEmpty: raise Ex('your matrix is empty')
        if sizeTemp == (1, 1): return self[0]
        if sizeTemp == (2, 2): return (self[0][0] * self[1][1]) - (self[1][0] * self[0][1])
        if mTemp[0][0] == 0:
            for row in range(sizeTemp[0]):
                if mTemp[row][0] != 0:
                    mTemp[row], mTemp[0] = mTemp[0], mTemp[row]
            if mTemp[0][0] == 0:
                return 0
            detMul = -1
        result = 0
        for row in range(1, sizeTemp[0]):
            mulTemp = mTemp[row][0] / mTemp[0][0]
            for col in range(sizeTemp[1]):
                mTemp[row][col] -= mTemp[0][col] * mulTemp

        return mTemp[0][0] * Matrix.filter(self.__data, 0, 0).determineG() * detMul

    def determineR(self):
        sizeTemp = self.size
        if self.isEmpty: raise Ex('your matrix is empty')
        if sizeTemp == (1, 1): return self[0]
        if sizeTemp == (2, 2): return (self[0][0] * self[1][1]) - (self[1][0] * self[0][1])
        return self.determineG()
        indexTemp = sizeTemp[0]-1
        matTemp = Matrix.filter(self.__data, 0, 0)
        divTemp = Matrix.filter(matTemp.mData, matTemp.size[0]-1,matTemp.size[0]-1).determineR()
        if divTemp == 0:
            return 'we can\'t find solution with this method'
        return Matrix([[Matrix.filter(self.__data, 0, 0).determineR(),
                        Matrix.filter(self.__data, indexTemp, 0).determineR()],
                       [Matrix.filter(self.__data, 0, indexTemp).determineR(),
                       Matrix.filter(self.__data, indexTemp, indexTemp).determineR()]]).determineR() / divTemp

    def __add__(self, other):
        if not isinstance(other, Matrix): raise TypeError('please give two Matrix form')
        elif self.size != other.size: raise Ex('Matrix must have same size for adding')
        temp = []
        for i in range(self.size[0]):
            temp2 = []
            for j in range(self.size[1]):
                temp2.append(self[i][j] + other[i][j])
            temp.append(temp2)
        return Matrix(temp)

    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('please give two Matrix form')
        elif self.size != other.size:
            raise Ex('Matrix must have same size for adding')
        temp = []
        for i in range(self.size[0]):
            temp2 = []
            for j in range(self.size[1]):
                temp2.append(self[i][j] + other[i][j])
            temp.append(temp2)
        return Matrix(temp)

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('please give two Matrix form')
        elif self.size != other.size:
            raise Ex('Matrix must have same size for adding')
        temp = []
        for i in range(self.size[0]):
            temp2 = []
            for j in range(self.size[1]):
                temp2.append(self[i][j] + other[i][j])
            temp.append(temp2)
        return Matrix(temp)


    def __mul__(self, other):
        pass


    def __imul__(self, other):
        pass

    def __rmul__(self, other):
        pass


    def __sub__(self, other):
        if not isinstance(other, Matrix): raise TypeError('please give two Matrix form')
        elif self.size != other.size: raise Ex('Matrix must have same size for adding')
        temp = []
        for i in range(self.size[0]):
            temp2 = []
            for j in range(self.size[1]):
                temp2.append(self[i][j] - other[i][j])
            temp.append(temp2)
        return Matrix(temp)

    def __isub__(self, other):
        if not isinstance(other, Matrix): raise TypeError('please give two Matrix form')
        elif self.size != other.size: raise Ex('Matrix must have same size for adding')
        temp = []
        for i in range(self.size[0]):
            temp2 = []
            for j in range(self.size[1]):
                temp2.append(self[i][j] - other[i][j])
            temp.append(temp2)
        return Matrix(temp)

    def __rsub__(self, other):
        if not isinstance(other, Matrix): raise TypeError('please give two Matrix form')
        elif self.size != other.size: raise Ex('Matrix must have same size for adding')
        temp = []
        for i in range(self.size[0]):
            temp2 = []
            for j in range(self.size[1]):
                temp2.append(self[i][j] - other[i][j])
            temp.append(temp2)
        return Matrix(temp)




    def __str__(self):
        return str(self.__data)
    
    def __repr__(self):
        return self.__data

