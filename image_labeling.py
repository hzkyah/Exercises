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

def neighboors(matrix, i, j):
    length = len(matrix)
    width = len(matrix[0]) 
    if i < length - 1 and j < width - 1:
        return [(i, j+1), (i+1, j), (i+1, j+1)]
    if i == length - 1 and j < width - 1:
        return [(i, j+1)]
    if j == width - 1 and i < length - 1:
        return [(i+1, j)]
    return []

def shade_neighbours(matrix, i, j, shade_value):
    peers = neighboors(matrix, i, j)
    if len(peers) > 0:
        for coord in peers:
            if matrix[coord[0]][coord[1]] == 1:
                shade_neighbours(matrix, coord[0], coord[1], shade_value)
    matrix[i][j] = shade_value
    
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
