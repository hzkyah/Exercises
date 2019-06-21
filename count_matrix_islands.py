# Enter your code here. Read input from STDIN. Print output to STDOUT
# Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Input:
# 11110
# 11010
# 11000
# 00000


# start reading from top left as an entry into the land vs sea map
# if you get the edge of a land try to register all it connected land neighboors, if not already registered
# continue doing this for all matrix element 

def get_peers(r, c, matrix):
    R = len(matrix)
    C = len(matrix[0])
    
    top = r - 1 if r > 0 else r
    down = r + 1 if r < R - 1 else r
    left = c - 1 if c > 0 else c
    right = c + 1 if c < C - 1 else c
                                        # get all peers having a land value  
    land_coordinates = [(r,c) for c in range(left, right+1) for r in range(top, down+1) if matrix[r][c] == 1]
    return land_coordinates

def register_island(pos, matrix, visited):
    peers = get_peers(pos[0], pos[1], matrix)
    visited.add(pos)
    while peers:
        peer = peers.pop()
        if peer not in visited:
            register_island(peer, matrix, visited)

def count_islands(matrix):
    R = len(matrix)
    C = len(matrix[0])
    visited = set()
    island = 0
    for r in range(R):
        for c in range(C):
            if matrix[r][c] and (r, c) not in visited:
                island += 1
                register_island((r, c), matrix, visited)
    return island

mat = [[1,1,0,0,0],
       [1,1,0,1,1],
       [0,0,0,0,0],
       [0,0,0,1,1]]

print(count_islands(mat))
