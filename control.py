from matris import Matrix

# x = Matrix([
#     [12,48,100],
#     [7,5,22.5],
#     [7,5.12,7.23]
# ])
#
# x = Matrix([
#     [10,1,3,-7],
#     [5,4,1,12],
#     [0,2,10,11],
#     [4,3,20,11]
# ])

x = Matrix('C:\\Users\\Windows\\Desktop\\s\\hard\\-8085868037132687.0.txt')
# x = [
#     [5, 11, 0],
#     [4, 57, 5],
#     [4, 27, 2]
# ]

# x = Matrix([
#     [1, -1, 8],
#     [0, 3, 1],
#     [2, 2, 1]
# ])

y = Matrix([
    
])
# x[1], x[0] = x[0], x[1]
print(x.size)
print(x.determineRC())
print(x.determineG())
print(x.determineR())
