# Image labeling problem: Given an array, label each distinct region in a 2D image of 1's 
# and 0's with a different number. You may assume that the only adjacent possibilities 
# are up, down, left, or right (no diagonals). For example:

#input array
#[[0, 1, 0, 0, 0, 0, 1],
# [0, 1, 1, 0, 0, 0, 0],
# [0, 1, 0, 0, 0, 0, 0],
# [0, 1, 0, 0, 0, 1, 1],
# [0, 0, 0, 0, 0, 1, 0],
# [0, 0, 0, 0, 0, 1, 0]]

#desired output array
#[[0, 2, 0, 0, 0, 0, 4],
# [0, 2, 2, 0, 0, 0, 0],
# [0, 2, 0, 0, 0, 0, 0],
# [0, 2, 0, 0, 0, 3, 3],
# [0, 0, 0, 0, 0, 3, 0],
# [0, 0, 0, 0, 0, 3, 0]]

import itertools

def neighboors(matrix, row, col):
    length = len(matrix)
    width = len(matrix[0]) 
    left = col - 1 if col - 1 >= 0 else col
    right = col + 1 if col + 1 < width else col
    top = row - 1 if row - 1 >= 0 else row
    bottom = row + 1 if row + 1 < length else row
    coordinates = itertools.product([row, top, bottom], [col, left, right])
    coordinates = set(coordinates)

    return coordinates

def shade_neighbours(matrix, row, col, shade_value):
    peers = neighboors(matrix, row, col)
    matrix[row][col] = shade_value
    if len(peers) > 0:
        for coord in peers:
            if matrix[coord[0]][coord[1]] == 1:
                shade_neighbours(matrix, coord[0], coord[1], shade_value)
    
def matrix_function(matrix):
    length = len(matrix)
    width = len(matrix[0])
    next_block = 1
    for i in range(length):
        for j in range(width):
            if matrix[i][j] == 1:
                next_block += 1
                shade_neighbours(matrix, i, j, next_block)
    return matrix

m = [[0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0]]

result = matrix_function(m)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end='')
    print()
