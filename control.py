from matris import Matrix

x = Matrix([
    [12,48,100],
    [7,5,22.5],
    [7,5.12,7.23]
])

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
